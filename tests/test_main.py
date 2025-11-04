from app.main import greet


def test_greet():
    """Testa se a função greet retorna a saudação esperada."""
    assert greet() == "Olá, DevOps! Bem-vindo à Aula 05."
