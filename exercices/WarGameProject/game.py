from player import Player

class Game:

    def __init__(self, players: [Player]):
        self.players = players

    def play_game(self, offset):
        """
        """
        for player in self.players:
            while player.has_cards():
                picked_cards = player.play(offset)
                print("Player {} picked:".format(player.name))
                for c in picked_cards:
                    print("\t"+ str(c))