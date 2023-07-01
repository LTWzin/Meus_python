participantes = [
    'Jonas', 'Juan', 'Yami', 'Witalo', 'Carlos', 'Pedro', 'Submarino do iberê', 'Rafael', 'Jao', 'Eto', 'lampada do pisca', 'café', 'vasco'
    ]
for pessoa in participantes:
    if pessoa == 'Witalo':
        print (pessoa + ", oporra")
    else:
        print (pessoa.title() + ", você está na lista!")
print ("\n" + str(len(participantes)) + " participantes no total!")