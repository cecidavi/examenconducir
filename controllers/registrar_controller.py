from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models.registrar_model import crear_usuario

# Creamos un Blueprint para la ruta
usuarios_bp = Blueprint('usuarios', __name__)

# Ruta para crear un usuario
@usuarios_bp.route('/crear', methods=['GET', 'POST'])
def crear_usuario_controller():
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        email = request.form['email']
        telefono = request.form['telefono']
        contrasena = request.form['contrasena']

        # Validaciones básicas (debes agregar más según sea necesario)
        if not nombre or not paterno or not materno or not email or not telefono or not contrasena:
            flash('Por favor, completa todos los campos.', 'danger')
            return redirect(url_for('usuarios.crear_usuario_controller'))

        # Encriptamos la contraseña
        contrasena_hash = generate_password_hash(contrasena)

        # Llamamos a la función para crear el usuario
        if crear_usuario(nombre, paterno, materno, email, telefono, contrasena_hash):
            flash('Usuario creado exitosamente!', 'success')
            return redirect(url_for('usuarios.crear_usuario_controller'))
        else:
            flash('Hubo un error al crear el usuario.', 'danger')
            return redirect(url_for('usuarios.crear_usuario_controller'))

    return render_template('crear_est.html')  # Muestra el formulario de creación de usuario
