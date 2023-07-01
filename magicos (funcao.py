magicos = ['arthur', 'pyong', 'fabio', 'annya']
mostrar_magicos= []
while magicos:
    aparecer = magicos.pop()
    mostrar_magicos.append(aparecer)
def nome(nomes):
    for nome in nomes:
        print (nome)
def apresentacao(magos):
    for magic in magos:
        print ("O grande " + magic + "!")
apresentacao(mostrar_magicos)
print ("----------------------")
nome(mostrar_magicos)
    