
from ai_player import Ai_player
from human_player import Human

class Game:

    def __init__(self) -> None:
        self.player_one_gesture = ''
        self.player_two_gesture = ''
    
    
    def choosing_the_players(self):
        self.number_of_players = input(f'choose the number of players from 0-2')
        if self.number_of_players == '0':
            self.player_one_gesture = Ai_player.choosing_gesture()
            self.player_two_gesture = Ai_player.choosing_gesture()
        elif self.number_of_players == "1":
            self.player_one_gesture = Human.gesture()
            self.player_two_gesture = Ai_player.choosing_gesture()
        elif self.number_of_players == "2":
            self.player_one_gesture = Human.gesture()
            self.player_two_gesture = Human.gesture()


    def collecting_gestures(self):
        pass

    def compare_choices(self):
        pass
