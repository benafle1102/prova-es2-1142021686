
MINIMO = 12

def senha_valida(senha):
    if not senha:
        return False
    return len(senha) >= MINIMO
