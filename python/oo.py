class PrimeiraClasse:
    pass

objeto1 = PrimeiraClasse()
objeto2 = PrimeiraClasse()

class Pessoa:
    def andar(self):
        print('Pessoa andou um passo')

joao = Pessoa()
print(joao.andar)
joao.nome = "Joao da Silva"
print(joao.__dict__)


class Pessoa:
    email = ''
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    def andar(self):
        print('Pessoa andou um passo')
    
    def tem_coracao(self):
        return True
    
    def __repr__(self):
        return(self._nome)

    def __str__(self):
        return(self._nome) 

maria = Pessoa('Mariazinha','123456')

class Professor:
    def tem_coracao(self):
        return False

class PessoasBoas(Professor, Pessoa):
    pass

orlando = PessoasBoas('Orlando','123546')