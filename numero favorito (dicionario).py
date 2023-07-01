witalo= {
    'nome': 'witalo', 'sobrenome': 'gabriel', 'idade': '16', 'cidade': 'barreiras'}
num_fav= {
    'laisy': 34, 'davi': 26, 'vinicius': 13, 'calli':5, 'felipe':53}

print ("Sou o " + witalo['nome'] + " " + witalo['sobrenome'] 
 + ", tenho " + str(witalo['idade']) + " anos e moro em " + 
witalo['cidade'] + "."
)
for pessoa in num_fav:
    print (pessoa + ", seu numero favorito é: "  + str(num_fav[pessoa]))
