#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from WarGameProject.deck import Deck
from WarGameProject.player import Player
from WarGameProject.game import Game
from WarGameProject.hand import Hand
from WarGameProject.constants import Constants

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
d = Deck()
(hand1, hand2) = d.split_deck()
p1 = Player("ADAN", Hand(hand1))
p2 = Player("ROG", Hand(hand2))
print("Player {} has {} cards".format(p1, p1.hand.len()))
print("Player {} has {} cards".format(p2, p2.hand.len()))
game = Game({p1.name: p1, p2.name: p2})

game.play_game(2)