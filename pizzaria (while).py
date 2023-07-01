ativo = True
print ("Digite 'pronto' para terminar sua pizza!")
while ativo == True:
    pedido = input("Qual o sabor da pizza?\n")
    if pedido == 'pronto':
        print ("Sua pizza está sendo enviada!")
        break
    else:
        print ("Colocando " + pedido.upper() + " na sua pizza")