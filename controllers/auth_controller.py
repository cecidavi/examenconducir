from flask import request, redirect, url_for, flash, session
from models.database import create_connection

def login_user():
    email = request.form['username']
    password = request.form['password']
    
    connection = create_connection()
    cursor = connection.cursor()
    
    try:
        # Consulta para verificar las credenciales
        cursor.execute(
            "SELECT * FROM estudiante WHERE email = %s AND contrasena = %s",
            (email, password)
        )
        user = cursor.fetchone()
        
        if user:
            session['username'] = email
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('estudiante'))  # Cambia 'dashboard' por tu página principal
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            return redirect(url_for('index'))
    finally:
        cursor.close()
        connection.close()