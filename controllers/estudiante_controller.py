# controllers/estudiante_controller.py

from flask import Blueprint, render_template, session, redirect, url_for
from models.registrar_model import obtener_matricula_por_email
from models.examen_model import (
    contar_intentos,
    obtener_historial_estudiante,
    obtener_respuestas_de_intento
)

estudiante_bp = Blueprint('estudiante', __name__)

@estudiante_bp.route('/estudiante')
def estudiante():
    if 'username' not in session:
        return redirect(url_for('index'))

    email = session['username']
    matricula = obtener_matricula_por_email(email)

    intentos_practica = contar_intentos(matricula, "practica")
    intentos_final = contar_intentos(matricula, "final")

    return render_template('estudiante.html',
                           matricula=matricula,
                           email=email,
                           intentos_practica=intentos_practica,
                           intentos_final=intentos_final)


# ✅ Nueva ruta: historial de intentos
@estudiante_bp.route('/historial')
def historial():
    if 'username' not in session:
        return redirect(url_for('index'))

    email = session['username']
    matricula = obtener_matricula_por_email(email)
    historial = obtener_historial_estudiante(matricula)

    return render_template('historial.html', historial=historial)


# ✅ Nueva ruta: ver respuestas de un intento
@estudiante_bp.route('/ver_respuestas/<int:id_record>')
def ver_respuestas(id_record):
    if 'username' not in session:
        return redirect(url_for('index'))

    respuestas = obtener_respuestas_de_intento(id_record)
    return render_template('ver_respuestas.html', respuestas=respuestas)
