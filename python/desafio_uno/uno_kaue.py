import random
tipo=["Normal","Coringa","Especial"]
cores=["Azul","Vermelho","Verde","Amarelo"]
numeros = [1,2,3,4,5,6,7,8,9]
coringa=["+4","trocaCor"]
especial=["bloqueio","+2","retorno"]

class Cartas:
    def __init__(self):
        self.tipo = tipo[random.randint(0,2)]
        if self.tipo == "Normal":
            self.cor = cores[random.randint(0,3)]
            self.numero = numeros[random.randint(0,8)]

        elif self.tipo == "Especial":
            self.cor = cores[random.randint(0,3)]
            self.tipo = especial[random.randint(0,2)]
                
        elif self.tipo == "Coringa":
            self.tipo = coringa[random.randint(0,1)]
        pass
    
    '''Cria Baralho com 108 cartas aleatorias'''
class Baralho:
    def __init__(self):
        self.cartas = []
        for x in range (108):
            self.cartas.append(Cartas())
    pass

b = Baralho()
for x in range (108):
    print (b.cartas[x].__dict__)
   
