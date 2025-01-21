# Player Class
# Attributes --> Name, Deck for currently owned cards, deck for war cards.

# Methods: 
# 1. Add cards won(single or many)
# 2. Play cards in a gamephase

class Player:

    # This helps to keep all the players cards
    def __init__(self, name):

        # This is to distinguish between players
        self.name = name

        # This is to hold all your cards
        self.cardslist = [ ]

        # This temporarily holds all cards risked in a war
        self.warcards = [ ]

        print(f'{name} joined the game')

    # If you win a war or if you win an exchange, you can add your opponents cards to your deck
    # Also, this appends your cards to the bottom of the deck(Rightmost of a list)
    def add_cards(self, cards_won):
        # This will add one lists values to another list regardless of how many elements are within it
        if type(cards_won) == type([ ]):
            self.cardslist.extend(cards_won)

        # Single Card added
        else:
            self.cardslist.append(cards_won)


    # When playing war, you typically take the top card of your deck. In this case, the leftmost of your cardslist
    def play_card(self):
        return self.cardslist.pop(0)


    def __str__(self):
        return f'Player {self.name} has {len(self.cardslist)} card(s).'
