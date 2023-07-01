class dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def sentar(self):
        print (self.nome + " está agora sentado(a)!")
    def rolar(self):
        print (self.nome + " está rolando!")
meu_dog= dog( 'moona', 1)
print ("O nome da minha cadela é " + meu_dog.nome.title())
print ("Minha cachorra tem " + str(meu_dog.idade) + " ano(s)!")
print (meu_dog.sentar())
print (meu_dog.rolar())
