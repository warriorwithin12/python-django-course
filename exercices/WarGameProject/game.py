from .player import Player
from .card import Card
from .constants import Constants
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

    def play_game(self):
        """
        This function contains the main logic of War Card Game.

        We iterate over rounds if every player has cards to play.
        In each round every player pick up offset cards from his mount and face up one.
        After that, we check if we have a winner of the current round or a battle (same card value). 
        If we have battle, we store the previous cards to a stack for the next winner (who appends it to his mount) and continue to next round.
        The looser is the player who don't have any more cards to continue playing.
        """
        round = 0
        offset = Constants.INITIAL_PICK_CARDS_OFFSET
        stacked_cards = []
        while self.next_round_available(offset):
            round += 1
            print("\n> Playing round {} {}".format(round, '(in a battle)' if stacked_cards else ''))
            
            picked_cards = {}
            # Every player picks offset cards 
            for name, player in self.players.items(): picked_cards[name] = player.play(offset)
            # Face up a random card by each player
            face_up = self.__face_up_cards(picked_cards)
            # Sort faced up cards to determine winner of current round (highest card value is the winner)
            sorted_face_up = list(face_up.items())            
            sorted_face_up.sort(key=lambda x: card_sort(x[1]), reverse=True)
            # Check if we have a war comparing tuples of cards
            is_war = reduce(lambda x,y: x[1].value == y[1].value, sorted_face_up)
            # If we have war, save current picked cards from all players and continue to next round
            if (is_war):
                for player, cards in picked_cards.items(): stacked_cards.extend(cards)
                print("> WE HAVE A BATTLE! Accumulated cards: {}".format(' // '.join(map(str, stacked_cards))))
                offset += 1
                # TODO: Special case when we have a BATTLE in the last round (one player has no more cards available than offset)
                # if self.next_round_available(offset) == False:
                #     offset = Constants.INITIAL_PICK_CARDS_OFFSET
                continue
            else:
                i = 0
                # If we don't had war previously, it means we have a winner
                # The first player in sorted_face_up is the winner, so we append all played cards to his hand.
                for (player, cards) in sorted_face_up:
                    player = self.players.get(player)
                    # Check if we had war in previous round and append played cards + previous ones
                    if stacked_cards and i == 0:
                        self.__append_win_cards(player, picked_cards.items())
                        player.hand.cards.extend(stacked_cards)
                        stacked_cards.clear()
                        print("\t{} wins the battle!".format(player))
                    # In simple round, we append all played cards to winners hand
                    elif i == 0:
                        self.__append_win_cards(player, picked_cards.items())
                    print("\t{}({}) with {} {}".format(player, player.hand.len(), cards, 'is the winner of round '+ str(round) if i == 0 else ''))
                    i += 1
                # Reset the picking card offset to initial value
                offset = Constants.INITIAL_PICK_CARDS_OFFSET
                
        # Return the winner of the War Game
        return self.__get_winner()
        

    def next_round_available(self, offset):
        """
        Checks if every player have cards and the offset of next picked cards,
        it's in range to continue playing.
        """
        checked_players = list(map(lambda player: player.hand.len() >= offset, list(self.players.values())))
        return all(checked_players)

    def __face_up_cards(self, picked_cards):
        """
        Get a randomized face up card from the picked previous ones.
        """
        face_up = {}
        for name, player in self.players.items():
            shuffle(picked_cards[name])
            face_up[name] = picked_cards[name][0]          
        return face_up

    def __append_win_cards(self, winner, cards):
        """
        Assign the cards to the winner.
        """
        for p, win_cards in cards: winner.hand.cards.extend(win_cards)

    def __get_winner(self):
        """
        Gets the winner of card players.
        The winner it's the one with the highest number of cards in his hand.
        """
        players = list(self.players.values())
        return reduce(lambda p1,p2: p1 if p1.hand.len() > p2.hand.len() else p2, players)