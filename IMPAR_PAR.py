from random import randint
ganhou = 0
cpujogada = 0
while True:
    escolha = int(input('''
[1] Par
[2] Impar
Digite sua escolha: '''))
    if escolha != 1 and escolha != 2:   #jogadas invalidas
        print('Digite um valor valido!')
        break
    jogada = int(input('Digite seu número a ser jogado: '))
    cpujogada = randint(0, 6)   #Todas as jogadas de numeros possiveis em uma mão
    resultado = jogada + cpujogada   #Soma da jogada da cpu e do jogador
    if escolha == 1 and resultado % 2 == 0:   #Se o resultado for par e escolha for par
        print('Você ganhou!')
        print(f'A cpu jogou {cpujogada}')
        ganhou += 1
    elif escolha == 2 and resultado % 2 == 0:   #Se resultado for imopar e escolha for impar
        print('Você ganhou!')
        print(f'A cpu jogou {cpujogada}')
        ganhou += 1
    else:   #Qualquer outro resultado
        print('Você perdeu!')
        print(f'A cpu jogou {cpujogada} resultado em {cpujogada + jogada}')
        if ganhou == 0:
            print('Você perdeu de primeira!')
        else:
            print(f'Você ganhou {ganhou} vezes antes de perder!')
        break
print('Fim de jogo')
