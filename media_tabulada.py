alunos = list()
while True:
    nome = str(input('Digite o nome do aluno:  '))
    n1 = int(input('Nota 1 do aluno:  '))
    n2 = int(input('Nota 2 do aluno:  '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    continuar = str(input('Quer continuar? [S/N]   ')).upper()
    if continuar == 'N':
        break
print('-=' * 25)
print(f'{"N.":<4} {"NOME":<10} {"MEDIA":>11}')
for indice, aluno in enumerate(alunos):
    print(f'{indice:<4} {aluno[0]:<10} {aluno[2]:>10}')
while True:
    print('-=' * 25)
    busca = int(input('Deseja olhar as notas de qual aluno (Digite -1 para sair):  '))
    if busca == -1:
        print('Fim do Programa.')
        break
    if busca <= len(alunos) -1:
        print(f'Notas do Aluno {alunos[busca][0]} são {alunos[busca][1]}\n')