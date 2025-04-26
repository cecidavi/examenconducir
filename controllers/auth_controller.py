# controllers/auth_controller.py

from flask import request, redirect, url_for, flash, session
from models.database import create_connection
from werkzeug.security import check_password_hash  # 🔥 Importante

def login_user():
    email = request.form['username']
    password = request.form['password']
    
    connection = create_connection()
    cursor = connection.cursor()
    
    try:
        # Buscar al usuario por email
        cursor.execute(
            "SELECT contrasena FROM estudiante WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()
        
        if user and check_password_hash(user[0], password):
            session['username'] = email
            flash('✅ Inicio de sesión exitoso.', 'success')
            return redirect(url_for('estudiante'))
        else:
            flash('❌ Usuario o contraseña incorrectos.', 'danger')
            return redirect(url_for('index'))
    finally:
        cursor.close()
        connection.close()
