from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("Teste", 100) == "etseT"
    assert encrypt_message("Testando", 3) == "seT_odnat"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Testando a key com uma String", "A")
