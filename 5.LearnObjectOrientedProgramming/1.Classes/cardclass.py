"""
    I want to create a class that creates a deck of cards.
    
    When the deck is called, it should instantiate a full deck of 52 cards.
    
    The deck cannot be a dictionary as it needs to be ordered. Neither can it be a Set.
    The deck cannot be a tuple as I want the deck to be modifyable.
    Therefore the deck will be created with a list.

    e.g [card#1, card#2, card#3...]

    A cards' properties will be stored in a tuple. 
    This includes suit, rank. Value should be included for calculations but need not be presented to a user.

    (str(Rank), str(Suit), int(Value)) #How do i encode Aces

    other properties I've not considered yet.

"""
import random


class deckOfCards:
    
    def __init__ (self, seed):
        self.seed = seed
        self.cardset = [
            ("Ace", "Spades", 11),
            ("2", "Spades", 2),
            ("3", "Spades", 3),
            ("4", "Spades", 4),
            ("5", "Spades", 5),
            ("6", "Spades", 6),
            ("7", "Spades", 7),
            ("8", "Spades", 8),
            ("9", "Spades", 9),
            ("10", "Spades", 10),
            ("Jack", "Spades", 10),
            ("Queen", "Spades", 10),
            ("King", "Spades", 10),
            ("Ace", "Diamonds", 11),
            ("2", "Diamonds", 2),
            ("3", "Diamonds", 3),
            ("4", "Diamonds", 4),
            ("5", "Diamonds", 5),
            ("6", "Diamonds", 6),
            ("7", "Diamonds", 7),
            ("8", "Diamonds", 8),
            ("9", "Diamonds", 9),
            ("10", "Diamonds", 10),
            ("Jack", "Diamonds", 10),
            ("Queen", "Diamonds", 10),
            ("King", "Diamonds", 10),
            ("Ace", "Clubs", 11),
            ("2", "Clubs", 2),
            ("3", "Clubs", 3),
            ("4", "Clubs", 4),
            ("5", "Clubs", 5),
            ("6", "Clubs", 6),
            ("7", "Clubs", 7),
            ("8", "Clubs", 8),
            ("9", "Clubs", 9),
            ("10", "Clubs", 10),
            ("Jack", "Clubs", 10),
            ("Queen", "Clubs", 10),
            ("King", "Clubs", 10),
            ("Ace", "Hearts", 11),
            ("2", "Hearts", 2),
            ("3", "Hearts", 3),
            ("4", "Hearts", 4),
            ("5", "Hearts", 5),
            ("6", "Hearts", 6),
            ("7", "Hearts", 7),
            ("8", "Hearts", 8),
            ("9", "Hearts", 9),
            ("10", "Hearts", 10),
            ("Jack", "Hearts", 11),
            ("Queen", "Hearts", 12),
            ("King", "Hearts", 13)
        ]
    
        random.Random(self.seed).shuffle(self.cardset)


    def drawCard(self):
        return self.cardset.pop()

    def deckSize(self):
        return len(self.cardset)

"""
    def shuffle(self):
        random.shuffle(self.cardset)
"""
x = deckOfCards(1)

y = deckOfCards(1)

print(x.cardset)
print(y.cardset)

c1 = x.drawCard()
c2 = y.drawCard()

print(c1)
print(c2)
print(c1 == c2)


