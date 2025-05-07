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
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO historial_estudiante (matricula, calificacion, tipo_test, fecha_hora_realiza)
                VALUES (%s, %s, %s, NOW())
            """, (matricula, calificacion, tipo_test))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

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
            SELECT tipo_test, calificacion, fecha_hora_realiza
            FROM historial_estudiante
            WHERE matricula = %s
            ORDER BY fecha_hora_realiza DESC
        """, (matricula,))
        resultados = cursor.fetchall()
        for fila in resultados:
            historial.append({
                'tipo': fila[0],
                'calificacion': fila[1],
                'fecha': fila[2].strftime("%d/%m/%Y %H:%M")
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