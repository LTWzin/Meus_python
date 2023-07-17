h = 0
m = 0
s = 0
N = int(input('Digite o tempo solicitado em segundos: '))
while N > 3600:
    h += 1
    N -= 3600
while N > 60:
    m += 1
    N -= 60
while N >= 1:
    s += 1
    N -= 1
print('{}:{}:{}'.format(h, m, s))
