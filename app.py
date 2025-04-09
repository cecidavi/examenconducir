from flask import Flask, render_template, session, redirect, url_for
from controllers.auth_controller import login_user
from controllers.admin_controller import login_user as admin_login_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave segura

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

@app.route('/administrador')
def administrador():
    if 'username' in session:  # Verifica si el usuario ha iniciado sesión
        return render_template('administrador.html')  # Renderiza el archivo administrador.html
    else:
        return redirect(url_for('index'))  # Redirige al inicio si no ha iniciado sesión

@app.route('/login', methods=['POST'])
def login():
    return login_user()  # Llama a la lógica de inicio de sesión desde el controlador

@app.route('/logout')
def logout():
    session.pop('username', None)  # Cierra la sesión del usuario
    return redirect(url_for('index'))  # Redirige al inicio

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración