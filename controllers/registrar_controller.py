# controllers/registrar_controller.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models.registrar_model import crear_usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/crear', methods=['GET', 'POST'])
def crear_usuario_controller():
    if request.method == 'POST':
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        email = request.form['email']
        telefono = request.form['telefono']
        contrasena = request.form['contrasena']

        if not nombre or not paterno or not materno or not email or not telefono or not contrasena:
            flash('❌ Por favor, completa todos los campos.', 'danger')
            return redirect(url_for('usuarios.crear_usuario_controller'))

        contrasena_hash = generate_password_hash(contrasena)

        if crear_usuario(nombre, paterno, materno, email, telefono, contrasena_hash):
            flash('✅ Usuario creado exitosamente. Ahora inicia sesión.', 'success')
            return redirect(url_for('index'))  # 🔥 Redirige a login (index)
        else:
            flash('❌ Hubo un error al crear el usuario.', 'danger')
            return redirect(url_for('usuarios.crear_usuario_controller'))

    return render_template('crear_est.html')
