import pytest
from flask import Flask
from flask_testing import TestCase
from controllers.examen_controller import simulador_bp

class TestSimulador(TestCase):
    def create_app(self):
        # Crear una instancia de la aplicación de Flask
        app = Flask(__name__)
        app.secret_key = '1282'
        
        # Registrar el blueprint
        app.register_blueprint(simulador_bp)
        
        return app
    
    def test_simulador(self):
        # Simular la solicitud GET
        response = self.client.get('/simulador/practica')
        
        # Verificar que la respuesta tenga un código de estado 200
        self.assertEqual(response.status_code, 200)
        
        # Verificar que las preguntas estén en la respuesta
        self.assertIn(b'Por favor, responde todas las preguntas cuidadosamente', response.data)
