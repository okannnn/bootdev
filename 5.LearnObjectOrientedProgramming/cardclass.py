"""
    I want to create a class that creates a deck of cards.
    
    When the deck is called, it should instantiate a full deck of 52 cards.
    
    The deck cannot be a dictionary as it needs to be ordered. Neither can it be a Set.
    The deck cannot be a tuple as I want the deck to be modifyable.
    Therefore the deck will be created with a list.

    e.g [card#1, card#2, card#3...]

    A cards' properties will be stored in a tuple. 
    This includes suit, rank. Value should be included for calculations but need not be presented to a user.

    (str(Rank), str(Suit), int(Value)) #How do i encode Aces?

    other properties I've not considered yet.

    #issues
    I had deckOfCards defined as a global variable. When more than one instance of a deck was instantiated, functions applied to one object affected all other objects. 
        Resolved by creating __init__ function. Unsure if the __init__ is needed for this, but is also used to define a seed for deterministic shuffling of cards.

        "Static variables are shared by every instance of the class."
        "Instance variables are defined only within methods, so __init__ or any other class function is required to make a object dependent variable."

    random.Random() is a local random number generator which produces the same values given the input. By doing this, it creates a deterministic randomness to be used consistently.
    This is likely needed to be moved elsewhere where needed, but for now functions as a seeded randomiser for a shuffle.
    random.shuffle() is used to return a reordered list, which is now determined by random.Random(seed).

    drawCard function removes a card from the deck and returns the card tuple.
        There isn't a method to restore the deck to original decksize. It may be that a reference copy of the cardset may be needed to restore from so that cards can be reintroduced into the deck.

"""
import random
#Random used to shuffle a new instance of a deck.

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
            ("Jack", "Hearts", 10),
            ("Queen", "Hearts", 10),
            ("King", "Hearts", 10)
        ]
    
        random.Random(self.seed).shuffle(self.cardset)


    def drawCard(self):
        return self.cardset.pop()

    def deckSize(self):
        return len(self.cardset)
    
    def shuffle(self):
        random.Random(self.seed).shuffle(self.cardset)

    def drawCards(self, n):
        self.__tempHand = []

        for i in range(1, n+1):
            self.__tempHand.append(self.drawCard())
        
        return self.__tempHand


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
"""

