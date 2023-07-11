from random import randint
from time import sleep
print('=-' * 11)
jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA''')
jogada = int(input('Digite sua jogada: '))
computador = randint(0, 2)
print('+-' * 11)
print('PEDRA, ')
sleep(0.6)
print('PAPEL, ')
sleep(0.6)
print('TESOURA ! !')
print('\033[2mO computador jogou {}\033[m'.format(jogadas[computador]))
print('\033[2mO jogador jogou {}\033[m'.format(jogadas[jogada]))
print('+-' * 11)
if computador == 0: #Computador joga pedra
    if jogada == 0:
        print('\033[33;2mEMPATE!\033[m')
    elif jogada == 1:
        print('\033[32;2mJogador ganhou!\033[m')
    elif jogada == 2:
        print('\033[31;2mComputador ganhou!\033[m')
if computador == 1: #Computador joga papel
    if jogada == 0:
        print('\033[31;2mComputador ganhou!\033[m')
    elif jogada == 1:
        print('\033[33;2mEMPATE!\033[m')
    elif jogada == 2:
        print('\033[32;2mJogador ganhou!\033[m')
if computador == 2: #Computador joga tesoura
    if jogada == 0:
        print('\033[32;2mJogador ganhou!\033[m')
    elif jogada == 1:
        print('\033[31;2mComputador ganhou!\033[m')
    elif jogada == 2:
        print('\033[33:2mEMPATE!\033[m')
print('=-' * 11)
