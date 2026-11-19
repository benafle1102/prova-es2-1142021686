
MINIMO = 12

def senha_valida(senha):
    if not senha:
        return False
    return len(senha) >= MINIMO


# RF01: senhas com 12 ou mais caracteres devem ser aceitas.
# Correcao documentada na branch correcao-rf01-senha.
  
