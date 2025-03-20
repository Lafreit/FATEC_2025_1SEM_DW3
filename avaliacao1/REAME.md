# Avaliação 1

Desafio técnico para os alunos da disciplina "Desenvolvimento Web 3"

Na aula passada, o professor Orlando explicou passo-a-passo como consumir APIs com a linguagem Python e a biblioteca requests. O projeto exemplo foi o consumo da API Pokemon.

Neste diretório, há uma versão adaptada do projeto desenvolvido na aula passada, com uso do padrão de projeto Strategy.

O padrão de projeto Strategy é um padrão comportamental que permite definir uma família de algoritmos, encapsulá-los e torná-los intercambiáveis. Ele permite que um objeto altere seu comportamento em tempo de execução sem modificar seu código-fonte.

Em nosso projeto, novas classes que realizarão consumo de APIs poderão ser criadas, sem que nosso código main.py sofra grandes impactos.

Ao final do seu desenvolvimento, ao executar o código <b>main.py</b> a saída esperada será:

```console
Consumo da API Pokemon
****************************************
(1, 'bulbasaur')
(2, 'ivysaur')


Consumo da API Rick and Morty
****************************************
(1, 'Rick Sanchez', 'Human')
(2, 'Morty Smith', 'Human')


Consumo da API Star Wars
****************************************
('Luke Skywalker', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'])
('C-3PO', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])


Consumo da API Crônicas do Gelo e do Fogo
****************************************
('Jon Snow', ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', 'Season 6'])
('Walder', ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 6'])

```

### Atividades da Avaliação

1. Crie no seu github repositório com o nome <b>consumo_API_2025</b>

2. Utilize os códigos disponibilizados neste diretório como base ( main.py e API.py). Insira-os em seu repositório.

#### Realize o primeiro commit. 

    2. 1 Dica: Não se esqueça de manter os códigos no mesmo diretório.

    2. 2 Crie um ambiente virtual e instale a biblioteca requests, com uso do pip.

3. Implemente o método extract(self, id) da classe API_Rick_Morty. O método deve:

        3.1 Concatenar o ID à URL base para formar o endpoint correto.
    
        3.2 Fazer uma requisição GET para obter os dados no formato JSON.

        3.3 Retornar uma tupla contendo (id, name, species) do personagem.

        3.4 Tratar exceções para evitar que o programa quebre caso a API não responda corretamente.

#### Realize o segundo commit.

4. Implemente o método extract(self, id) da classe API_Star_Wars. O método deve:

        4.1 Concatenar o ID à URL base para formar o endpoint correto.
    
        4.2 Fazer uma requisição GET para obter os dados no formato JSON.

        4.3 Retornar uma tupla contendo (name, [ film(s) ]) do personagem.

        4.4 Tratar exceções para evitar que o programa quebre caso a API não responda corretamente.

#### Realize o terceiro commit.

5. Implemente o método extract(self, id) da classe API_Ice_and_Fire. O método deve:

        5.1 Concatenar o ID à URL base para formar o endpoint correto.
    
        5.2 Fazer uma requisição GET para obter os dados no formato JSON.

        5.3 Retornar uma tupla contendo (name, [ tvSeries ]) do personagem.

        5.4 Tratar exceções para evitar que o programa quebre caso a API não responda corretamente.

#### Realize o quarto commit.

Descomentar o trecho entre as linhas 19 e 31 no código main.py e observar se a saída de tela corresponde ao modelo apresentado no início deste README.

Elabore o <b>README.md</b>, com as instruções de como executar o projeto e outras informações que julgar necessárias. Gerar o arquivo <b>requirements.txt</b> (com as bibliotecas utilizadas por você) do seu repositório.

#### Realize o quinto e último commit.

Enviar a URL do seu portifólio na atividade no Teams até 22h30 do dia 20 de março de 2025. Só serão avaliados os repositórios presentes nesta atividade.