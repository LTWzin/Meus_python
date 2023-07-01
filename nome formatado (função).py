def nome_formatado(nome, final, sobrenome= ''):
    if sobrenome:
        nome_completo = (nome + " " + final + " " + sobrenome)
    else:
        nome_completo = (nome + " " + sobrenome + " " + final)
    return nome_completo.title()
pessoa = nome_formatado('witalo', 'gabriel')
print(pessoa)
print ("------------------------")
def saudacao(nomes):
    for nome in nomes:
        print ("Olá, " + nome + "!")
usuarios= ['Juan', 'carlos', 'remu', 'kirara']
saudacao(usuarios)
    