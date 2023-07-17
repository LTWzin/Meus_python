cidades = {77:'Barreiras', 61:'Brasilia', 71:'Salvador', 11:'Sao Paulo', 21:'Rio de Janeiro', 32:'Juiz de Fora', 19:'Campinas', 27:'Vitoria', 31:'Belo Horizonte'}
ddd = int(input('Digite o DDD cadastrado: '))
if ddd in cidades:
    print(cidades[ddd])
else: 
    print('DDD nao cadastrado')
