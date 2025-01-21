import Card
import random

# Deck Class
# Create and hold a 52 Card Object, Shuffle the deck, Deal Cards from the Deck Object

suit_card = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank_card = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
     
     # This creates a 52 card deck
    def __init__(self):
        self.all_cards = [ ]
        
        for suit in suit_card:
            for rank in rank_card:
                
                # Instantiates an Object
                card_object = Card.Card(suit, rank)

                # Adds the Card Object to our deck
                self.all_cards.append(card_object)

    # This prints every card in the deck
    # The reason this works is because we are taking advantage of the __str__ function from the Card class which will reveal the object's rank and suit
    # If an object is printed without having a built in str function or is not a string, we will only see its position in memory.
    def __str__(self):
        for card_obj in self.all_cards:
            print(card_obj)
        print()

    # Shuffling the deck
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        print('Deck was shuffled')

    # Dealing a card to a player
    # We can just forloop this later to split the deck between 2 people
    def deal_one(self):
        return self.all_cards.pop()
    