# controllers/estudiante_controller.py

from flask import Blueprint, render_template, session, redirect, url_for
from models.registrar_model import obtener_matricula_por_email
from models.examen_model import contar_intentos

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
