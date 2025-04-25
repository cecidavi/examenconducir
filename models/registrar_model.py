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
