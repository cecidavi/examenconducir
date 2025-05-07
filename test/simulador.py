import sys
import os

# Añadir la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from faker import Faker
from werkzeug.security import generate_password_hash
from models.database import create_connection
from models.examen_model import guardar_historial, guardar_respuesta
from models.examen_model import is_correct_answer, obtener_texto_respuesta

fake = Faker('es_MX')
usuarios_generados = []

def obtener_preguntas_y_respuestas():
    conn = create_connection()
    preguntas = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_pregunta FROM preguntas")
        ids = cursor.fetchall()
        for pid in ids:
            pregunta_id = pid[0]
            cursor.execute("SELECT id_respuesta FROM respuestas WHERE id_pregunta = %s", (pregunta_id,))
            respuestas = cursor.fetchall()
            if respuestas:
                preguntas.append({
                    'id_pregunta': pregunta_id,
                    'respuestas': [r[0] for r in respuestas]
                })
        cursor.close()
        conn.close()
    return preguntas

def insertar_estudiante(nombre, email):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        contrasena_segura = generate_password_hash('1234')  # contraseña encriptada válida

        cursor.execute("""
            INSERT INTO estudiante (nombre, paterno, materno, email, telefono, contrasena)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, fake.last_name(), fake.last_name(), email, fake.msisdn()[:10], contrasena_segura))
        conn.commit()
        cursor.execute("SELECT LAST_INSERT_ID()")
        matricula = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        usuarios_generados.append({'email': email, 'password': '1234'})  # guardar para imprimir
        return matricula
    return None

def simular_examen(matricula, tipo_test, cantidad_preguntas, max_intentos, puntos_por_pregunta):
    preguntas = obtener_preguntas_y_respuestas()
    for _ in range(random.randint(1, max_intentos)):
        seleccionadas = random.sample(preguntas, cantidad_preguntas)
        correctas = 0
        id_record = guardar_historial(matricula, 0, tipo_test)  # guardamos primero

        for item in seleccionadas:
            id_pregunta = item['id_pregunta']
            id_respuesta = random.choice(item['respuestas'])  # aleatorio
            if is_correct_answer(id_respuesta):
                correctas += 1
            texto = obtener_texto_respuesta(id_respuesta)
            guardar_respuesta(id_pregunta, matricula, texto, id_respuesta, id_record)

        calificacion = correctas * puntos_por_pregunta
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE historial_estudiante
                SET calificacion = %s
                WHERE id_record = %s
            """, (calificacion, id_record))
            conn.commit()
            cursor.close()
            conn.close()

def simular_alumnos_y_examenes(n):
    for _ in range(n):
        nombre = fake.first_name()
        email = fake.unique.email()
        print(f"Generando alumno: {nombre} - {email}")
        matricula = insertar_estudiante(nombre, email)
        if matricula:
            simular_examen(matricula, "practica", 20, 6, 5)
            simular_examen(matricula, "final", 40, 3, 2.5)

if __name__ == "__main__":
    simular_alumnos_y_examenes(10)  # Cambia 10 si quieres más

    print("\nUsuarios generados para iniciar sesión:")
    for usuario in usuarios_generados:
        print(f"Email: {usuario['email']} | Contraseña: {usuario['password']}")
