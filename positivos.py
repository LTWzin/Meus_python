zero = 0
numeros = []
positivo = 0
for pergunta in range(0, 6):
    n = float(input('Digite um numero qualquer:  '))
    if n > 0:
        numeros.append(n)
    elif n == 0:
        zero = 1
print('{} valores positivos'.format(len(numeros)))
if zero == 1:
    print('Zero (0) é nulo!')