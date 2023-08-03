jogador = {}
todos = []
partidajogador = 0
gols = []
totalgol = 0
partida = 1
while True:
    nome = str(input('Digite o nome do jogador:  ')).title()
    quantia = int(input(f'Quantas partidas {nome} jogou:  '))
    jogador['nome'] = nome
    for cont in range(0, quantia):
        gol = int(input(f'Quantos gols {jogador["nome"]} fez na partida {cont + 1}:  '))
        gols.append(gol)
        totalgol += gol
    jogador['score'] = gols[:]
    jogador['total'] = totalgol
    todos.append(jogador.copy())
    jogador.clear()
    gols.clear()
    totalgol = 0
    continuar = str(input('Deseja adicionar outro jogador na lista? [S/N]   ')).upper().strip()
    if continuar == 'N':
        break
print('-=' * 25)
print(f'{"N.":<4}{"NOME":<9}{"GOLS":>6}')
for indice, jogador in enumerate(todos):
    print(f'{indice:<4}{jogador["nome"]:<9}{jogador["total"]:>6}')
while True:
    busca = int(input('Deseja olhar os gols das partidas de qual jogador (-1 para parar):   '))
    if busca == -1:
        break
    if busca <= len(todos) -1:
        print(f'O jogador {todos[busca]["nome"]} fez:')
        for g in todos[busca]["score"]:
            partidajogador += 1
            print(f'Na partida {partidajogador} fez {g} gols')
        partidajogador = 0
    else:
        print('Número invalido! Tente Novamente:  ')
print('=-FIM DO PROGRAMA-=')