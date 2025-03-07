'''
Inspirado no Baralho Pythonico do Luciano Ramalho:
https://pythonfluente.com/#ex_pythonic_deck 
'''
import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class UnoDeck:
    colors = 'red green yellow blue'.split()
    action_cards = ['Skip', 'Reverse', 'Draw Two']
    special_cards = ['Wild', 'Wild Draw Four']

    def __init__(self):
        self._cards = []

        for color in self.colors:
            for number in range(1, 10): 
                self._cards.append(Card(str(number), color))
            self._cards.append(Card('0', color))

        for color in self.colors:
            for action in self.action_cards:
                self._cards.append(Card(action, color))
                self._cards.append(Card(action, color))

        for special in self.special_cards:
            for _ in range(4):  # Quatro cartas especiais
                self._cards.append(Card(special, 'wild'))
        random.shuffle(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)
        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = UnoDeck()

print(len(deck))  
print(deck[0])  

for card in deck._cards[0:5]:
    print(card)

deck.shuffle()
for card in deck._cards[0:5]:
    print(card)
'''
import random
random.shuffle(deck._cards)
for i in range(5):
    print(deck[i])
'''