p1 = 0
p2 = 1
cn = 3
print('-'*24)
print(' Sequência de Fibonacci')
print('-'*24)
ns = int(input('Digite quantos numeros da sequencia você quer ver: '))
print('{} - {} - '.format(p1, p2), end= '')
while cn <= ns:
    p3 = p1 + p2
    print('{} - '.format(p3), end= '')
    p1 = p2 
    p2 = p3
    cn += 1
print('\033[32mFim!\033[m')
