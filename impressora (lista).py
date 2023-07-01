pedidos = ['celular', 'dinossauro', 'carta', 'carro', 'caixa']
completos= []
while pedidos:
    design_atual = pedidos.pop()
    print ("Imprimindo agora: " + design_atual)
    completos.append(design_atual)
    print ("Os seguintes modelos estão prontos:")
for completo in completos:
    print(completo)