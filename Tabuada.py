n = int(input('Digite um numero: '))
o = 0
for num in range(0, n* 11):
    if num % n == 0:
        print('{} x {} = {}'.format(n, o, num))
        o += 1
        