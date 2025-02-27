numero1 = 10
numero2 = 5.6
numero3 = 10 + 3j
print(type(numero1))
print(type(numero2))
print(type(numero3))

nome = 'Fatec'
'''
Em Python, string é um objeto imutável
'''
''' 
Inserir seu nome completo em uma string e capturar apenas
o primeiro nome.
'''
nome = 'Orlando Saraiva'
print(nome[0:7])
print(nome.split(' ')[0])

''' Lista são mutáveis'''
lista = []
lista.append('pão')
lista.append('leite')
lista.append(100)
lista.append([1,2,3])
print(lista[-1][1])

''' Tuplas são objetos imutáveis'''

tupla = (1,2,3)
for item in tupla:
    print(item)

lista2 = list(tupla)
lista2.append(4)
lista2.append(5)
tupla = tuple(lista2)


lista3 = []
for x in range(10):
    lista3.append(x)
    lista3.append(x + 1)

''' Desafio: Remover todos os itens duplicados de lista3'''

listTemp = []
for x in lista3:
    if x not in listTemp:
        listTemp.append(x)

''' O mesmo desafio com set '''
lista4 = list(set(lista3))

''' Dicionário '''
fatec = {}
fatec['orlando'] = ['DW2','DW3']
fatec['nilton'] = 'algoritmo'
fatec['thiago'] = ('Banco NoSQL','CoordenadorSI')
fatec['horarios'] = {'orlando':['DW2','DW3'],'nilton':'Algoritmo'}
