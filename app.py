from flask import Flask, render_template, session, redirect, url_for
from controllers.auth_controller import login_user
from controllers.registrar_controller import usuarios_bp

app = Flask(__name__)
app.secret_key = '1282'  # Cambia esto por una clave segura

# Registra el Blueprint de usuarios
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

@app.route('/')
def index():
    return render_template('index.html')  # Renderiza el archivo index.html

@app.route('/estudiante')
def estudiante():
    if 'username' in session:  # Verifica si el usuario ha iniciado sesión
        return render_template('estudiante.html')  # Renderiza el archivo estudiante.html
    else:
        return redirect(url_for('index'))  # Redirige al inicio si no ha iniciado sesión

@app.route('/prueba')
def prueba():
    if 'username' in session:  # Verifica si el usuario ha iniciado sesión
        return render_template('prueba.html')  # Renderiza el archivo estudiante.html
    else:
        return redirect(url_for('index'))  # Redirige al inicio si no ha iniciado sesión

@app.route('/presentar-examen')
def presentar_examen():
    if 'username' in session:
        return render_template('examen.html')
    else:
        return redirect(url_for('index'))

@app.route('/registrarse')
def registrarse():
    return render_template('crear_est.html')  # Suponiendo que tienes un template para el registro


@app.route('/login', methods=['POST'])
def login():
    return login_user()  # Llama a la lógica de inicio de sesión desde el controlador

@app.route('/logout')
def logout():
    session.pop('username', None)  # Cierra la sesión del usuario
    return redirect(url_for('index'))  # Redirige al inicio

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración
