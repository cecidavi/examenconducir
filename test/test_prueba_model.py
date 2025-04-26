import pytest
from models.examen_model import get_random_questions

# Simulamos la conexión a la base de datos
@pytest.fixture
def mock_database_connection(monkeypatch):
    # Aquí puedes mockear la función `create_connection` si es necesario
    pass

def test_get_random_questions(mock_database_connection):
    preguntas = get_random_questions(5)  # Por ejemplo, obtenemos 5 preguntas
    assert len(preguntas) == 5, "Debe devolver 5 preguntas"
    
    # Verificar que cada pregunta tiene respuestas
    for pregunta in preguntas:
        assert 'respuestas' in pregunta, "Cada pregunta debe tener respuestas"
        assert len(pregunta['respuestas']) > 0, "Cada pregunta debe tener al menos una respuesta"
