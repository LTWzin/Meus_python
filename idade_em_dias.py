idade = int(input('Digite a idade em dias: '))
a = idade // 365
idade = idade - a * 365
m = idade // 30 
idade = idade - m * 30
d = idade
print('Ano: {}'.format(a))
print('Mes: {}'.format(m))
print('Dia: {}'.format(d))
