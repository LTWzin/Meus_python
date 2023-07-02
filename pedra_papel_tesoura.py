import random
print("""=========================
|PEDRA | PAPEL | TESOURA|
=========================""")
adversario = str(input('Digite sua jogada: '))
maquina = random.randint(1, 3)
adversario = adversario.lower()
if maquina == 1:
    acao = 'papel'
if maquina == 2:
    acao = 'pedra'
if maquina == 3:
    acao = 'tesoura'
print('A maquina jogou {}'.format(acao))
if adversario == 'papel':
    if maquina == 1:
        print('Empate!')
    if maquina == 2:
        print('Você ganhou!')
    if maquina == 3:
        print('Você perdeu!')
if adversario == 'pedra':
    if maquina == 1:
        print('Você perdeu!')
    if maquina == 2:
        print('Empate!')
    if maquina == 3:
        print('Você ganhou!')
if adversario == 'tesoura':
    if maquina == 1:
        print('Você ganhou!')
    if maquina == 2:
        print('Você perdeu!')
    if maquina == 3:
        print('Empate!')
        