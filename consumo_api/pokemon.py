import requests
import csv

URL_BASE = 'https://pokeapi.co/api/v2/pokemon/'

list_pokemon = []
for i in range(1, 1026):
    URL = URL_BASE + str(i)
    try:
        dado = requests.get(URL).json()
        list_pokemon.append((dado.get('id'), dado.get('name')))
    except:
        pass
    

with open('pokemon.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for pokemon in list_pokemon:
        writer.writerow(pokemon)

f = open("pokemon.txt", "w")
for pokemon in list_pokemon:
    f.write(str(pokemon[0]) + '   ' + str(pokemon[1] + '\n'))
f.close()