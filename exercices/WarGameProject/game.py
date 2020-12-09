from .player import Player
from .card import Card
from random import shuffle
from functools import cmp_to_key, reduce

# Define custom Card value sort function
def card_sort(x: Card):
    if x.value.isnumeric(): 
        return int(x.value)
    else: 
        if (x.value == 'J'): return 11
        elif (x.value == 'Q'): return 12
        elif (x.value == 'K'): return 13
        elif (x.value == 'A'): return 14
        else: return 0

class Game:
    """
    Main Game class.
    Contains the logic of the War Game between players.
    """
    def __init__(self, players):
        self.players = players

    def play_game(self, offset):
        """
        """
        round = 0
        stacked_cards = []
        while self.next_round_available(offset):
            round += 1
            print("> Playing round {}, accumulated cards: {}".format(round, ' // '.join(map(str, stacked_cards))))
            
            picked_cards = {}
            # Every player picks offset cards 
            for name, player in self.players.items(): picked_cards[name] = player.play(offset)
            # Face up a random card by each player
            face_up = self.__face_up_cards(picked_cards)
            # Sort faced up cards to determine winner of current round. 
            sorted_face_up = list(face_up.items())            
            sorted_face_up.sort(key=lambda x: card_sort(x[1]))
            # Check if we have a war
            # Compare tuples of cards
            is_war = reduce(lambda x,y: x[1].value == y[1].value, sorted_face_up)
            if (is_war):
                print("\t> WE HAVE WAR!!!")
                for player, cards in picked_cards.items():                    
                    stacked_cards.extend(cards)
                offset += 1
            else:
                i = 0
                for (player, cards) in sorted_face_up:
                    print("\t{}: {} {}".format(player, cards, 'winner!' if i == 0 else ''))
                    # Check if we had war in previous round and append the stacked cards to winner hand
                    # Reset the picking card offset to initial value
                    if stacked_cards and i == 0:
                        winner = self.players.get(player)
                        winner.hand.cards.extend(stacked_cards)
                        stacked_cards.clear()
                        offset = 2
                        print("THE WINNER OF ROUND {} IS {}".format(round, winner))
                    i+=1
                
                    
            # print('; '.join(map(str, sorted_face_up)))

    def next_round_available(self, offset):
        """
        Checks if every player have cards and the offset of next picked cards,
        it's in range to continue playing.
        """
        checked_players = list(map(lambda player: player.has_cards() and player.hand.len() >= offset, list(self.players.values())))
        return all(checked_players)

    def __face_up_cards(self, picked_cards):
        """
        Get a randomized face up card from the picked previous ones.
        """
        face_up = {}
        for player in self.players:
            shuffle(picked_cards[player])
            face_up[player] = picked_cards[player][0]          
        return face_up