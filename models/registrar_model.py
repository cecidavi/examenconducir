from models.database import create_connection

def crear_usuario(nombre, paterno, materno, email, telefono, contrasena):
    conn = None
    cursor = None
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO estudiante (nombre, paterno, materno, email, telefono, contrasena)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (nombre, paterno, materno, email, telefono, contrasena))
        conn.commit()
        print("✅ Usuario creado exitosamente!")
        return True

    except Exception as e:
        print("❌ Error al crear usuario:", e)
        if conn:
            conn.rollback()
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obtener_matricula_por_email(email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT matricula FROM estudiante WHERE email = %s", (email,))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        cursor.close()
        conn.close()
