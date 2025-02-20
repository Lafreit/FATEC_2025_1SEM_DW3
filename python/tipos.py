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

