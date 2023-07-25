numeros = [[], [], []]   #Desafio: Matriz usando apenas uma lista!
numesquerdo = numdireito = posicao = 0
print('-=' * 5)
print('| Matriz |')
print('-=' * 5)
for c in range(0, 9):   #Pergunta 9x
    num = int(input(f'Digite um valor para [{numesquerdo}, {numdireito}]:  '))
    numeros[posicao].append(num)   #Guarda  o valor em uma das posiçoes da lista
    numdireito += 1
    if numdireito == 3:   #Onde o maximo de itens dentro da lista dentro da lista é 3
        numesquerdo += 1  #Com 3 listas para organização
        numdireito = 0
        posicao += 1
print('-=' * 13)   #MATRIZ
print('      0     1     2')
print(f'\n0   [ {numeros[0][0]} ] [ {numeros[0][1]} ] [ {numeros[0][2]} ]')
print(f'1   [ {numeros[1][0]} ] [ {numeros[1][1]} ] [ {numeros[1][2]} ]')
print(f'2   [ {numeros[2][0]} ] [ {numeros[2][1]} ] [ {numeros[2][2]} ]')
