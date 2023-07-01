nome = input ("Qual o seu nome? \n") #Input= entrada
if nome:
    print ("Seu nome é " + nome.title() + "!\n") #Saída
else:
    print ("Escreva algo na caixa")
    exit()
idade = input("Qual a sua idade? \n") #Entrada
idade = int(idade) #Transformar um inteiro em string
if idade <= 18: #se idade menor que 18
    print ("Você só tem " + str(idade) + " anos!")
else:
    print ("Você é maior de idade e tem " + str(idade) + " ano(s)!")