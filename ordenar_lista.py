posi = 0
numeros = []
for cont in range(0, 5):
    posi += 1 
    n = int(input(f'Digite o {posi}o numero: '))
    if cont == 0:   #Se for o primeiro numero
        numeros.append(n)
    elif n > numeros[-1]:   #Se o numero digitado é maior que o ultimo item da lista
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):   #Procurar entre todos os itens da lista
            if n <= numeros[pos]:   #Se o numero digitado é maior que o item da posição
                numeros.insert(pos, n)
                break
            pos += 1

print('-=' * 13)
print('Os numeros digitados (Em ordem) foram: {}'.format(numeros))
