# controllers/prueba_controller.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.examen_model import get_random_questions, is_correct_answer, guardar_historial, contar_intentos
from models.registrar_model import obtener_matricula_por_email

prueba_bp = Blueprint('prueba', __name__)

@prueba_bp.route('/prueba', methods=['GET', 'POST'])
def prueba():
    if 'username' not in session:
        return redirect(url_for('index'))

    email = session['username']
    matricula = obtener_matricula_por_email(email)

    # Verificar número de intentos antes de dejar pasar
    intentos_practica = contar_intentos(matricula, "practica")
    if intentos_practica >= 6:
        flash('❌ Ya has alcanzado el máximo de 6 intentos para la práctica.', 'danger')
        return redirect(url_for('estudiante'))

    if request.method == 'POST':
        respuestas = request.form
        correctas = 0
        total = len(respuestas)

        for pregunta_id in respuestas:
            respuesta_id = int(respuestas[pregunta_id])
            if is_correct_answer(respuesta_id):
                correctas += 1

        # Calificación de prueba práctica: 5 puntos por reactivo correcto
        calificacion = correctas * 5

        # Guardar resultado
        guardar_historial(matricula, calificacion, "practica")

        # Mensaje de resultado
        if calificacion >= 75:
            flash(f'✅ ¡Aprobaste la prueba con {calificacion}%!', 'success')
        else:
            flash(f'❌ No aprobaste la prueba. Tu calificación fue {calificacion}%.', 'danger')

        return redirect(url_for('estudiante'))

    preguntas = get_random_questions(20)
    return render_template('prueba.html', preguntas=preguntas)
