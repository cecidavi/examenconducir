from models.database import create_connection

def get_random_questions(limit):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            # Traer preguntas + ruta de imagen con JOIN
            cursor.execute("""
                SELECT p.id_pregunta, p.reactivo, b.ruta
                FROM preguntas p
                LEFT JOIN banco_imagenes b ON p.codigo_imagen = b.codigo_imagen
                ORDER BY RAND() LIMIT %s
            """, (limit,))
            preguntas = cursor.fetchall()

            datos = []
            for pregunta in preguntas:
                pregunta_id, texto, ruta = pregunta

                # Obtener respuestas asociadas
                cursor.execute("SELECT id_respuesta, opcion FROM respuestas WHERE id_pregunta = %s", (pregunta_id,))
                respuestas = cursor.fetchall()

                # Construir ruta si existe
                imagen = f"{ruta}" if ruta else None

                datos.append({
                    'id': pregunta_id,
                    'texto': texto,
                    'imagen': imagen,
                    'respuestas': [{'id': r[0], 'texto': r[1]} for r in respuestas]
                })

            return datos

        finally:
            cursor.close()
            conn.close()
    return []

def is_correct_answer(respuesta_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ok FROM respuestas WHERE id_respuesta = %s", (respuesta_id,))
            result = cursor.fetchone()
            return result and result[0] == 1
        finally:
            cursor.close()
            conn.close()
    return False

def guardar_historial(matricula, calificacion, tipo_test):
    conn = create_connection()
    id_record = None
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO historial_estudiante (matricula, calificacion, tipo_test, fecha_hora_realiza)
                VALUES (%s, %s, %s, NOW())
            """, (matricula, calificacion, tipo_test))
            conn.commit()
            id_record = cursor.lastrowid  # Captura el ID generado
        finally:
            cursor.close()
            conn.close()
    return id_record  # Lo devolvemos para usarlo después


def contar_intentos(matricula, tipo_test):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM historial_estudiante
                WHERE matricula = %s AND tipo_test = %s
            """, (matricula, tipo_test))
            result = cursor.fetchone()
            return result[0] if result else 0
        finally:
            cursor.close()
            conn.close()
    return 0

def obtener_historial_estudiante(matricula):
    conn = create_connection()
    historial = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_record, tipo_test, calificacion, fecha_hora_realiza
            FROM historial_estudiante
            WHERE matricula = %s
            ORDER BY fecha_hora_realiza DESC
        """, (matricula,))
        resultados = cursor.fetchall()
        for fila in resultados:
            historial.append({
                'id_record': fila[0],  # <- esto es lo que faltaba
                'tipo': fila[1],
                'calificacion': fila[2],
                'fecha': fila[3].strftime("%d/%m/%Y %H:%M")
            })
        cursor.close()
        conn.close()
    return historial


def ha_aprobado_examen_final(matricula):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT 1 FROM historial_estudiante
                WHERE matricula = %s AND tipo_test = 'final' AND calificacion >= 75
                LIMIT 1
            """, (matricula,))
            resultado = cursor.fetchone()
            return resultado is not None
        finally:
            cursor.close()
            conn.close()
    return False

def guardar_respuesta(id_pregunta, matricula, respuesta_texto, id_respuesta, id_record):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO examen_estudiante (id_pregunta, matricula, respuesta, id_respuesta, id_record)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_pregunta, matricula, respuesta_texto, id_respuesta, id_record))
            conn.commit()
        finally:
            cursor.close()
            conn.close()


def obtener_texto_respuesta(id_respuesta):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT opcion FROM respuestas WHERE id_respuesta = %s", (id_respuesta,))
            result = cursor.fetchone()
            return result[0] if result else ""
        finally:
            cursor.close()
            conn.close()

def obtener_respuestas_de_intento(id_record):
    conn = create_connection()
    respuestas = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                p.reactivo,
                r.opcion AS respuesta_usuario,
                r.ok,
                b.ruta AS imagen
            FROM examen_estudiante e
            JOIN preguntas p ON e.id_pregunta = p.id_pregunta
            JOIN respuestas r ON r.id_respuesta = e.id_respuesta
            LEFT JOIN banco_imagenes b ON p.codigo_imagen = b.codigo_imagen
            WHERE e.id_record = %s
        """, (id_record,))
        for fila in cursor.fetchall():
            respuestas.append({
                'pregunta': fila[0],
                'respuesta': fila[1],
                'correcta': bool(fila[2]),
                'imagen': fila[3]
            })
        cursor.close()
        conn.close()
    return respuestas
