
from ai_player import Ai_player
from human_player import Human

class Game:

    def __init__(self) -> None:
        self.player_one_gesture = ''
        self.player_two_gesture = ''
    
    def choosing_the_players(self):
        self.number_of_players = input(f'choose the number of players from 0-2')
        if self.number_of_players == '0':
            self.player_one = Ai_player()
            self.player_two = Ai_player()  
  
        elif self.number_of_players == '1':
            self.player_one = Human()
            self.player_two = Ai_player() 

        elif self.number_of_players == '2':
            self.player_one = Human()
            self.player_two = Human()       


    def collecting_gestures(self):
        self.player_one_gesture = self.player_one.choosing_gesture()
        self.player_two_gesture = self.player_two.choosing_gesture()
        

        print(self.player_one_gesture)
        print(self.player_two_gesture)
        
        

    def compare_choices(self):
        pass
