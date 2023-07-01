Mensagem= "hello world!" 

print (Mensagem)

mensage2= "hello \nearth!    " #\n é quebra de linha

print (mensage2)
#print = executar uma mensagem
print ("--------------------------------------------")

print (mensage2.title()) #função title deixa em maiusculo a primeira letra 
print (Mensagem.title())

print (mensage2.upper())#função upper deixa tudo em maiusculo
print (Mensagem.lower())#função lower deixa tudo em minusculo

print ("--------------------------------------------")

Texto= (mensage2.title().rstrip() + ", " + Mensagem.title())#rstrip retira espaços desnecessarios da direita

print (Texto)

print ("\tEveryone!".upper())#\t é um 'tab'' na execução