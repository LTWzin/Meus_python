n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n3) / 3
print('Sua media é de nota \033[1;35m{:.1f}\033[m'.format(m))
if m >= 6:
    print('\033[32;1mPARABENS!\033[m')
else:
    print('\033[31;1mESTUDE MAIS!\033[m')