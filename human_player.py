from player import Player

class Human:
    def __init__(self) -> None:
        self.gesture = ''

    def choosing_gesture(self):
        gestures_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        
        gesture_index =input(f'Press 0 for {gestures_list[0]}, Press 1 for {gestures_list[1]},\n Press 2 for {gestures_list[2]}, Press 3 for {gestures_list[3]}, Press 4 for {gestures_list[4]}  ') 
        self.gesture = gestures_list[gesture_index]
        print(self.gesture)

