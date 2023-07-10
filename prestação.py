casa = float(input('Digite o valor da casa desejada (em Reais): '))
salario = float(input('Digite o seu salario mensal: '))
parcelas = float(input('Em quantos anos você irá parcelar:  '))
t = parcelas * 12
p = casa / t
s = salario * 0.30
if p < s:
    print('O valor da prestação ficou de R${:.2f} pagando por {:.0f} meses.'.format(p, t))
    print('Seu emprestimo foi aprovado!')
else:
    print('O seu pedido de prestação foi negado.')