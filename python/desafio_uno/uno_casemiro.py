
class Carta:
    def __init__(self, simbolo, cor):
        self.simbolo = simbolo
        self.cor = cor

    def __str__(self):
        return f'{self.cor} {self.simbolo}'

class CartaEspecial(Carta):
    def __init__(self, simbolo, cor, acao):
        super().__init__(simbolo, cor)
        self.acao = acao
    def __str__(self):
        return f'{self.cor} {self.simbolo}'

class Baralho:
    def __init__(self):
        self.cartas = []
        for cor in ['vermelho', 'azul', 'verde', 'amarelo']:
            for simbolo in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.cartas.append(Carta(simbolo, cor))
                self.cartas.append(Carta(simbolo, cor))
            
            for simbolo in ['Inverter', 'Bloqueio']:
                    self.cartas.append(CartaEspecial(simbolo, cor, simbolo))
                    self.cartas.append(CartaEspecial(simbolo, cor, simbolo))

            self.cartas.append(CartaEspecial('Compra 2', cor, 'comprar +2'))
            self.cartas.append(CartaEspecial('Compra 2', cor, 'comprar +2'))

        self.cartas.append(CartaEspecial('Compra 4', 'preto', 'comprar +4'))
        self.cartas.append(CartaEspecial('Compra 4', 'preto', 'comprar +4'))
        self.cartas.append(CartaEspecial('Coringa', 'preto', 'Altera a cor atual'))
        self.cartas.append(CartaEspecial('Coringa', 'preto', 'Altera a cor atual'))
        
    def __str__(self):
        print('Baralho:')
        for carta in self.cartas:
            print(carta.__str__())
        


print(Carta('5', 'vermelho').simbolo)
print(Carta('5', 'vermelho').cor)
assert Carta('5', 'vermelho').simbolo == '5'
assert Carta('5', 'vermelho').cor == 'vermelho'
print(CartaEspecial('C', 'preto', 'comprar +4').simbolo)
print(CartaEspecial('C', 'preto', 'comprar +4').cor)
assert CartaEspecial('C', 'preto', 'comprar +4').simbolo == 'C'
assert CartaEspecial('C', 'preto', 'comprar +4').cor == 'preto'
assert CartaEspecial('C', 'preto', 'comprar +4').acao == 'comprar +4'
baralho = Baralho()
print(baralho.__str__())
print(len(baralho.cartas))