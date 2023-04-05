from human_player import Human
from ai_player import Ai_player
from player import Player
from game import Game


game = Game()
game.choosing_the_players()
game.collecting_gestures()
game.compare_choices()