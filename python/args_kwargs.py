def soma(n1, n2):
    return n1 + n2

soma(1,2)
# soma(1,2,3) # Erro !
# Using *args allows to pass an arbitrary number of function arguments.

def soma(*args):
    total = 0
    for x in args:
        total = total + x
    return total

print(soma(1,2,3)) # 6
print(soma(1,2,3,4,5)) # 15

# KWArgs
# Using **kwargs allows to pass an arbitrary number of keyword arguments.

def imprime_dados(**kwargs):
    print(kwargs.get('nome','Não encontrado'))
    chaves = list(kwargs.keys())
    chaves = list(kwargs)
    for elemento in chaves:
        print(elemento + ':' + kwargs.get(elemento,'Não encontrado'))


imprime_dados(nome='Orlando')
imprime_dados(nome='Orlando',materia1='DW2')
imprime_dados(nome='Orlando',materia1='DW2',materia2='DW3')
