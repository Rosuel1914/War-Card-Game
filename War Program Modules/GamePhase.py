import Deck
import Player
import sys

# GamePhase Class
class GamePhase:
    # War the card game needs 2 players and a deck of cards. We'll Instantiate those as we create a GamePhase Object.
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        print('Game Start')
    
    # Both players play 1 card and their card will be revealed to the audience. Once played, the check_val will evaluate the card value.
    def play_a_card(self):
            card_1 = self.player1.play_card()
            card_2 = self.player2.play_card()
            print(f'{self.player1.name}({len(self.player1.cardslist)}) played a {card_1}')
            print(f'{self.player2.name}({len(self.player2.cardslist)}) played a {card_2}')
            print()

            return [card_1, card_2]

    # This checks which value between 2 cards played is higher. If equal, this will trigger the war method.
    def check_val(self, c1, c2):
        
        # Player 1 wins exchange
        if c1.values > c2.values:
            print(f'{self.player1.name} won this exchange')

            # Player 1 will add his card and his opponent's card to the bottom of his deck
            self.player1.add_cards(c1)
            self.player1.add_cards(c2)

            # This is for the war bool. The second number is for war method only
            return [False, 1]

        # Player 2 wins exchange
        elif c1.values < c2.values:
            print(f'{self.player2.name} won this exchange')
            
            # Player 2 will add his card and his opponent's card to the bottom of his deck
            self.player2.add_cards(c1)
            self.player2.add_cards(c2)

            return [False, 0]
        
        # If both cards are equal
        else:
            # Will store the current equal cards in the war cards list
            self.player1.warcards.append(c1)
            self.player2.warcards.append(c2)
            # This will make war = True
            return [True]

    def war_phase(self):
        # Buffer
        print()
        print('______________________________________________________')
        input('War Phase will commence. Press Enter to continue. ')
        print()
        print('Both players must have 4 cards to continue, or else you automatically lose the game.')
        print()

        # You need 4 cards to go to war. If not, then you lose the game
        # If player 1 doesn't have enough cards, player 2 wins
        if len(self.player1.cardslist) < 4:
            print(f'{self.player1.name}({len(self.player1.cardslist)}) doesn''t have enough cards to go to war and has lost the card game')
            print()
            print(f'{self.player2.name}(52) has won')
            # Exits the program once the game ends
            print()
            print('Game End')
            sys.exit()
                

        # Else if player 2 doesn't have enough cards, player 1 wins   
        elif len(self.player2.cardslist) < 4:
            print(f'{self.player2.name}({len(self.player2.cardslist)}) doesn''t have enough cards to go to war and has lost the card game')
            print()
            print(f'{self.player1.name}(52) has won')
            # Exits the program once the game ends
            print()
            print('Game End')
            sys.exit()


        # Place 3 cards in the war pile
        print('Place 3 cards in the war pile.')
        print()
        for number in range(3):
            # war cards will be kept in a list temporarily(aka, each player in the game will put 3 cards face down to be part of the war)
            self.player1.warcards.append(self.player1.play_card())
            self.player2.warcards.append(self.player2.play_card())
            
        # Place 1 card as the final card to compare values
        print('Next, both players must play a 4th card.')
        print()
        a = self.play_a_card()

        # We evaluate the value of the 4th card.
        fourth_card = self.check_val(a[0],a[-1])

        # If we don't have another war, and player 1 wins:
        if fourth_card[0] == False and fourth_card[1] == 1:
            # Player 1 adds all his war cards and his opponents war cards to his main deck
            self.player1.add_cards(self.player1.warcards)
            self.player1.add_cards(self.player2.warcards)

            # We then clear both war card lists
            self.player1.warcards.clear()
            self.player2.warcards.clear()

            print(f'{self.player1.name} won the war and collects all cards')
            print()

        # If we don't have another war, and player 2 wins:
        elif fourth_card[0] == False and fourth_card[1] == 0:
            # Player 2 adds all his war cards and his opponents war cards
            self.player2.add_cards(self.player1.warcards)
            self.player2.add_cards(self.player2.warcards)

            # We then clear both war card lists
            self.player1.warcards.clear()
            self.player2.warcards.clear()
            
            print(f'{self.player2.name} won the war and collects all cards')
            print()
        else:
            # This is a recursion in case we have double or triple wars, etc.
            print('We have ourselves another war')
            print()
            self.war_phase()

    # This is the game itself. It will be in a while loop uptil someone triggers the condition for a win/loss.
    def play_game(self):

        # This splits the deck between the 2 players
        for num in range(26):
            self.player1.add_cards(self.deck.deal_one())
            self.player2.add_cards(self.deck.deal_one())

        print(f'Deck was evenly split between {self.player1.name} and {self.player2.name}')
        print()

        # This means that if player 1 doesn't lose all his cards or win all the cards, we will continue the game
        round = 1
        while len(self.player1.cardslist) not in (0, 52):
            print('______________________________________________________')

            print(f'Round {round}\n')
            
            # Both players play 1 card each
            part_1 = self.play_a_card() # In order to call a method within the same class/object, you need to prefix "self"

            # This compares the card values
            war = self.check_val(part_1[0], part_1[-1])

            # increment the round
            round +=1

            # This helps to pause the game so it doesn't just spam it. The audience can watch it at their own pace 
            input('Press Enter to continue to the next round. ')

            # This will check if there is war. Else it will skip.
            if war[0] is False:
                continue
            else:
                self.war_phase()

        # Once an opponents hand hits 0
        if len(self.player1.cardslist) == 0:
            print(f'{self.player2.name}(52) has collected all the cards and has won the game')
            print('Game End')
            sys.exit()

        # If player 1 didn't lose, they won all 52 cards
        else:
            print(f'{self.player1.name}(52) has collected all the cards and has won the game')
            print('Game End')
            sys.exit()
