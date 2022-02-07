import random as rand

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
values = [2,3,4,5,6,7,8,9,10,11,12,13,14]

class Owner:
    def __init__(self, name):
        self.name=name
        self.belongings = {}
    
    def __str__(self):
        return self.name
    
    def new_belonging(self,name, pile):
        self.belongings.update({name:pile})
    
    def draw_card(self, source, destination, amount):
        """Moves a card from the source pile to the destination pile"""
        while amount > 0:
            card = self.belongings[source].contents[0]
            self.belongings[destination].contents.append(card)
            self.belongings[source].contents.remove(card)
            amount -= 1

class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return str(self.value) + " of " + self.suit
    
class Pile:
    def __init__(self):
        self.contents = []
        self.size = len(self.contents)
    
    def __str__(self):
        print_string = ""
        if len(self.contents) == 0:
            return "Pile is empty"
        index = len(self.contents)
        for card in self.contents:
            if index > 1:
              print_string = print_string + str(card.value) + " of " + card.suit + "\n"
            else:
              print_string = print_string + str(card.value) + " of " + card.suit
            index -= 1    

        return print_string

    def shuffle(self):
        return rand.shuffle(self.contents)
    

class Deck(Pile):
    def __init__(self):
        self.contents = []
        self.size = len(self.contents)

    def build(self):
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.contents.append(card)

def shift_card(source, destination, amount):
    """Transfers an amount of cards from source pile to destination pile, e.g. shift_card(source["belonging"], destination["belonging"], 3)"""
    while amount > 0:
        card = source.contents[0]
        destination.contents.append(card)
        source.contents.remove(card)
        amount -= 1
        

def test():
    A = Owner("A")
    B = Owner("B")
    Board = Owner("Board")
    deck = Deck()
    deck.build()
    Board.new_belonging("Deck", deck)
    A.new_belonging("Hand", Pile()) 
    A.new_belonging("Discard", Pile())
    B.new_belonging("Hand", Pile())

    shift_card(Board.belongings["Deck"], A.belongings["Hand"], len(Board.belongings["Deck"].contents))
    print (A.belongings["Hand"])
    print(Board.belongings["Deck"])





