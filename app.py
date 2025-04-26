from flask import Flask, render_template, session, redirect, url_for
from controllers.auth_controller import login_user
from controllers.registrar_controller import usuarios_bp
from controllers.prueba_controller import prueba_bp
from controllers.final_controller import final_bp
from controllers.dashboard_controller import dashboard_bp
from controllers.estudiante_controller import estudiante_bp



app = Flask(__name__)
app.secret_key = '1282'

# Registrar Blueprints
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(prueba_bp)
app.register_blueprint(final_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(estudiante_bp)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estudiante')
def estudiante():
    if 'username' in session:
        return render_template('estudiante.html')
    else:
        return redirect(url_for('index'))

@app.route('/registrarse')
def registrarse():
    return render_template('crear_est.html')

@app.route('/login', methods=['POST'])
def login():
    return login_user()

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# (Opcional) Redirección desde presentar-examen a examen-final
@app.route('/presentar-examen')
def presentar_examen():
    return redirect(url_for('final.examen_final'))

if __name__ == '__main__':
    app.run(debug=True)
