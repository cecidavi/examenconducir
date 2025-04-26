# controllers/dashboard_controller.py

from flask import Blueprint, render_template, session, redirect, url_for
from models.registrar_model import obtener_matricula_por_email
from models.examen_model import obtener_historial_estudiante

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))

    email = session['username']
    matricula = obtener_matricula_por_email(email)
    historial = obtener_historial_estudiante(matricula)

    # Procesar datos
    intentos_practica = sum(1 for h in historial if h['tipo'] == 'practica')
    intentos_final = sum(1 for h in historial if h['tipo'] == 'final')
    
    promedio_practica = round(sum(h['calificacion'] for h in historial if h['tipo'] == 'practica') / intentos_practica, 2) if intentos_practica else 0
    promedio_final = round(sum(h['calificacion'] for h in historial if h['tipo'] == 'final') / intentos_final, 2) if intentos_final else 0

    return render_template('dashboard.html',
                           matricula=matricula,
                           email=email,
                           historial=historial,
                           intentos_practica=intentos_practica,
                           intentos_final=intentos_final,
                           promedio_practica=promedio_practica,
                           promedio_final=promedio_final)
