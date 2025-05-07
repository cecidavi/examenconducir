# controllers/final_controller.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.examen_model import (
    get_random_questions,
    is_correct_answer,
    guardar_historial,
    contar_intentos,
    ha_aprobado_examen_final,
    guardar_respuesta,
    obtener_texto_respuesta
)
from models.registrar_model import obtener_matricula_por_email

final_bp = Blueprint('final', __name__)

@final_bp.route('/examen-final', methods=['GET', 'POST'])
def examen_final():
    if 'username' not in session:
        return redirect(url_for('index'))

    email = session['username']
    matricula = obtener_matricula_por_email(email)

    # ✅ Verificar si ya aprobó el examen final
    if ha_aprobado_examen_final(matricula):
        flash('✅ Ya aprobaste el examen final. No necesitas volver a presentarlo.', 'info')
        return redirect(url_for('estudiante'))

    # Verificar número de intentos para final
    intentos_final = contar_intentos(matricula, "final")
    if intentos_final >= 3:
        flash('❌ Ya has alcanzado el máximo de 3 intentos para el examen final.', 'danger')
        return redirect(url_for('estudiante'))

    if request.method == 'POST':
        respuestas = request.form
        correctas = 0
        total = len(respuestas)

        for pregunta_id in respuestas:
            respuesta_id = int(respuestas[pregunta_id])
            if is_correct_answer(respuesta_id):
                correctas += 1

        # Calificación de examen final: 2.5 puntos por reactivo correcto
        calificacion = correctas * 2.5

        # ✅ Guardar resultado del intento y obtener su ID
        id_record = guardar_historial(matricula, calificacion, "final")

        # ✅ Guardar respuestas individuales
        for pregunta_id in respuestas:
            respuesta_id = int(respuestas[pregunta_id])
            texto_respuesta = obtener_texto_respuesta(respuesta_id)
            guardar_respuesta(
                int(pregunta_id),
                matricula,
                texto_respuesta,
                respuesta_id,
                id_record
            )

        # Mensajes de resultado
        if calificacion >= 75:
            flash(f'🎉 ¡Felicidades! Aprobaste el examen final con {calificacion:.2f}%. ¡Ahora puedes proceder al examen práctico de manejo!', 'success')
        else:
            flash(f'❌ No aprobaste el examen final. Tu calificación fue {calificacion:.2f}%.', 'danger')

        return redirect(url_for('estudiante'))

    preguntas = get_random_questions(40)
    return render_template('prueba.html', preguntas=preguntas)
