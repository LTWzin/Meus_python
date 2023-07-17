total = 0
maiormil = 0
menorvalor = 0
menornome = ''
print('-=' * 13)
print('''MERCADINHO QUE TEM TUDO!!''')
while True:
    print('-=' * 13)
    nome = str(input('Digite o nome do produto: '))
    preco = float (input('Digite o preço do(a) {}: '.format(nome)))
    if menorvalor == 0: 
        menorvalor = preco
        menornome = nome
    if preco < menorvalor:
        menorvalor = preco
        menornome = nome
    if preco > 1000:
        maiormil += 1
    total += preco
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]: '))
    if continuar == 'N': 
        break
print('-=' * 15)
print(f'O total foi de R${total:.2f}')
print(f'Existem {maiormil} itens mais caros que mil reais!')
print(f'O item mais barato é o item {menornome}, custando R${menorvalor:.2f}')
