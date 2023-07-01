numero_inicial = 0
numero_dado = input("Escreva um número!\n")
numero_dado = int(numero_dado)
while numero_inicial < numero_dado:
    numero_inicial += 1
    if numero_inicial % 2 != 0:
        print ("-" + str(numero_inicial))