from time import sleep   
from random import randint
jogos = list()   #Lista dos jogos
numero = list()  #Lista dos numeros sorteados
contador = 0
atual = 0
print('-=' * 16, '\nSORTEADOR DE NUMEROS DA MEGASENA', '\n',end= '' '-=' * 16)
quantidade = int(input('\nQual a quantia de jogos a ser sorteado?   '))
for quantia in range(0, quantidade):   #Quantos jogos serão feitos
    while True:
        if contador == 6:   #Limitar a quantia de numeros sorteados a 6
            break
        num = randint(1, 60)   #Sorteio
        if num not in numero:   #Se o numero ja foi sorteado ele não é adicionado a numeros
         numero.append(num)
        contador += 1  #Quantia de vezes sorteadas sobe em  1
    contador = 0   #Reinicia os numeros quando acaba
    numero.sort()   #Organiza em ordem crescente 
    jogos.append(numero[:])   #Adiciona uma copia dos numeros a lista jogos
    numero.clear()   #Reinicia os numeros sorteados
print('-=' * 6, '<SORTEANDO>', '-=' * 6)   
for i, n in enumerate(jogos):   #Mostra os jogos sorteados
    print(f'Seu {i + 1}º jogo sorteado: {n}')
    sleep(0.7)
print('=-=-=-=- <BOA SORTE!> -=-=-=-=')
