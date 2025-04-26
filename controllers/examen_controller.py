from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from models.examen_model import get_random_questions, is_correct_answer, guardar_historial

simulador_bp = Blueprint('simulador', __name__)

@simulador_bp.route('/simulador/<tipo>', methods=['GET', 'POST'])
@login_required
def simulador(tipo):
    if tipo not in ['practica', 'final']:
        return "Tipo de simulador no válido", 400

    cantidad = 20 if tipo == 'practica' else 40

    if request.method == 'POST':
        respuestas = request.form
        correctas = 0

        for pregunta_id in respuestas:
            respuesta_id = int(respuestas[pregunta_id])
            if is_correct_answer(respuesta_id):
                correctas += 1

        total = len(respuestas)
        calificacion = (correctas / total) * 100

        guardar_historial(current_user.id, calificacion, tipo)

        return render_template('resultado.html', calificacion=calificacion)

    preguntas = get_random_questions(cantidad)
    return render_template('prueba.html', preguntas=preguntas, tipo=tipo)
