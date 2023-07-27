alien= {'cor': 'verde', 'pontos': 5, 'velocidade': 'media'}
pontos= (alien['pontos'])

print ("O alien está da cor " + alien['cor'] + "!")
print ("\nVocê ganhou " + str(pontos) + " pontos!")
print ("-----------------------------------------------")
print (alien)
alien['cord_x']=0
alien['cord_y']=25
print (alien)
print ("-----------------------------------------------")
alien['cor']= 'amarelo'
print ("\nO alien está agora " + alien['cor'] + "!")
print ("Você ganhou mais "+ str(alien['pontos']) + " pontos!")
print("Original cord_x: " + str(alien['cord_x']))
if alien['velocidade'] == "lento":
    x_novo=1
elif alien['velocidade'] == "media":
    x_novo=2
else:
    x_novo=3
alien['cord_x'] = alien['cord_x'] + x_novo
print ("\no alien está agora na posição x: " + str(alien['cord_x']))
alien['velocidade']= "rapido"
del alien['cor']


