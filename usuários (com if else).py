usuarios= ['admin',  'chimera', 'gaules', 'tinows', 'eto']

if usuarios:
    for usuario in usuarios:
        if "admin" == usuario:
            print ("seja bem vindo, " + usuario.title() + ", gostaria de ver o relatorio de relatos?")
        else:
            print ("Seja bem vindo, " + usuario.title())
else: 
    print ("sem usuarios existentes, faça login!")   
        