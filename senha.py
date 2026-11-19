
MINIMO = 12

def senha_valida(senha):
    if not senha or not senha.strip():
        return False
    return len(senha) >= MINIMO
