print ("                ---------------")
print ("                --RESTAURANTE--")
print ("                ---------------\n")
qnt_pessoas= input("Quantos irão sentar na mesa?\n")
qnt_pessoas = int(qnt_pessoas)
if qnt_pessoas >= 7:
    print ("\nMesas para mais que 6 pessoas estão todas ocupadas, espere a sua vez na fila.")
elif qnt_pessoas == 1:
    print ("\nSomente você? Sua mesa já está pronta.")
else:
    print ("\nPoderiam me acompanhar até a sua mesa?")
    print ("Aqui está.")