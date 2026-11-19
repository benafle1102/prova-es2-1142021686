
from senha import senha_valida

def test_t1_senha_com_12_caracteres():
    assert senha_valida("123456789012") is True

def test_t2_senha_com_11_caracteres():
    assert senha_valida("12345678901") is False

def test_t3_senha_vazia():
    assert senha_valida("") is False
