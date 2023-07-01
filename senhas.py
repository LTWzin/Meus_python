senha = '12345'
def verificar_senha(minha_senha):
    if len(minha_senha) < 6:
        print ("Invalido")
    else:
        print ("Valida")