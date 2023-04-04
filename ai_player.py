import random
from player import Player

class Ai_player(Player):
    def __init__(self) -> None:
        self.gesture = ''
        super().__init__()
        

    def choosing_gesture(self):
        self.gesture = random.choice(self.gestures_list)
        print(self.gesture)


