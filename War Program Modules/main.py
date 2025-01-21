# Potentially put all of these in a function
import GamePhase
import Player
import Deck

# This is where the magic happens

# Create Deck
fresh_deck = Deck.Deck()

# Player Game
card_game = GamePhase.GamePhase(Player.Player('Sut'), Player.Player('Adrian'), fresh_deck)
print()

# Shuffle the Deck
fresh_deck.shuffle_deck()
print()

# Play game
card_game.play_game()

