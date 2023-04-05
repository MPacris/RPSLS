from player import Player

class Human(Player):
    def __init__(self) -> None:
        self.gesture = ''
        super().__init__()
        

    def choosing_gesture(self):
        gesture_index = input(f'Press 0 for {self.gestures_list[0]}, Press 1 for {self.gestures_list[1]},\n Press 2 for {self.gestures_list[2]}, Press 3 for {self.gestures_list[3]}, Press 4 for {self.gestures_list[4]}  ') 
        self.gesture = self.gestures_list[int(gesture_index)]
        print(self.gesture)


