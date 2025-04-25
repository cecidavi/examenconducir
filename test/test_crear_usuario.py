import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from models.registrar_model import crear_usuario

class TestCrearUsuario(unittest.TestCase):
    def test_crear_usuario_valido(self):
        resultado = crear_usuario("ejemplo", "apellidoeejemplo", "otravez", "aaaa@example.com", 8440000000, "0000")
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()
