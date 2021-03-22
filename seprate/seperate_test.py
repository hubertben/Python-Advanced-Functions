import random
from seperate import seperate

'''

class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    
    def __str__(self):
        return '{self.val} of {self.suit}'.format(self = self)


def init_cards(suits, vals, display):

    cards = []
    for s in suits:
        for v in vals:
            cards.append(Card(s, v))
            
    random.shuffle(cards)
    if(display):
        for c in cards:
            print(c)
    return cards



suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

cards = init_cards(suits, vals, True)

print('\n\n')

cards = seperate ( cards,  suits, 'suit')
for c in cards:
    print(c)


cards = seperate ( cards,  vals, 'val')
for c in cards:
    print(c)




class Pizza:

    def __init__(self, size, topping, side):
        self.size = size
        self.topping = topping
        self.side = side

    
    def __str__(self):
        return 'Pizza of size {self.size} with {self.topping} on top, and a side of {self.side}'.format(self = self)
    


siz = ['Small', 'Medium', 'Large', 'Extra Large']
top = ['Pepperoni', 'Mushrooms', 'Cheese', 'Peppers', 'Sausage', 'Bacon']
sid = ['Fries', 'Onion Rings', 'Garlic Bread']

pizzas = []

for i in range(100):
    pizzas.append(Pizza( random.choice(siz), random.choice(top), random.choice(sid) ))

pizzas = seperate ( pizzas,  top, 'topping')

for p in pizzas:
    print(p)


'''


class Planet:

    def __init__(self, size, loc, mass):
        self.size = size
        self.loc = loc
        self.mass = mass

    
    def __str__(self):
        if(self.loc == 1):
            return 'Planet is {self.size} meters in radius, and {self.loc}st away from the Sun, and has a mass of {self.mass}'.format(self = self)
        elif(self.loc == 2):
             return 'Planet is {self.size} meters in radius, and {self.loc}nd away from the Sun, and has a mass of {self.mass}'.format(self = self)
        
        return 'Planet is {self.size} meters in radius, and {self.loc}th away from the Sun, and has a mass of {self.mass}'.format(self = self)
    


size = [i for i in range(100000)]
loc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#mass = [200, 400, 800, 1600, 3200]
mass = [i for i in range(100000)]
planets = []

for i in range(1000):
    planets.append(Planet( random.choice(size), random.choice(loc), random.choice(mass) ))

planets = seperate ( planets,  size, 'size')

for p in planets:
    print(p)
