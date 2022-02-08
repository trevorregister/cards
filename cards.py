import random as rand

class Owner:
    """
    Parameters

    name (str): name of the Owner

    """
    def __init__(self, name):
        self.name=name
        self.belongings = {}
    
    def __str__(self):
        return self.name
    
    def new_belonging(self,name, pile):
        """
        Creates a new belonging.

        Parameters
        name (str):
        pile (Pile): Pile object. Can pass a previously created pile or just Pile().

        """
        self.belongings.update({name:pile})
    
    def draw_card(self, source, destination, amount):
        """
        Move one or more cards from a source pile to a destination pile, both of which must be within the owner's belongings.
        The top card of the source pile is placed on the bottom of the destination pile.

        Parameters
        source (str) - name of source belonging
        destination (str) - name of destination belonging
        amount (int) - number of cards to move.

        """
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
    """
    A Deck is specifically a standard 52-card deck of playing cards. Deck.build() creates a Pile
    who's contents is a sorted deck of cards, least to greatest, Clubs->Spades->Hearts->Diamonds.

    """

    def __init__(self):
        self.contents = []
        self.size = len(self.contents)

    def build(self):
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
        values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.contents.append(card)

def shift_card(source, destination, amount):
    """
    Transfers an amount of cards from source pile to destination pile. Used to move cards between owners. The top card of the source pile is placed
    on the bottom fo the destination pile.

    Parameters
    source (Pile) - source_owner.belongings["Belonging"]
    destination (Pile) - destination_owner.belongings["Belonging"]
    amount (int) - number of cards to move

    """
    while amount > 0:
        card = source.contents[0]
        destination.contents.append(card)
        source.contents.remove(card)
        amount -= 1





