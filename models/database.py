import mariadb
import sys

def create_connection():
    try:
        conn = mariadb.connect(
            user="cecilio",
            password="ceci1282",
            host="localhost",
            port=3306,
            database="simulacion"
        )
        print("Connection successful!")
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None  # Devuelve None en lugar de salir

# Example usage
if __name__ == "__main__":
    connection = create_connection()
    if connection:
        connection.close()
    else:
        print("Failed to connect to the database.")
