valores = []
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
valor3 = int(input('Digite um outro valor: '))
valores.append(valor1)
valores.append(valor2)
valores.append(valor3)
valores.sort()
print('-=' * 13)
print('{}\n{}  -->  Em ordem crescente\n{}'.format(valores[0], valores[1], valores[2]))
print('~~' * 13)
print('{}\n{}  -->  Como foi escrito\n{}'.format(valor1, valor2, valor3))
