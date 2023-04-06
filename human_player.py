
from player import Player

class Human(Player):
    def __init__(self) -> None:
        self.gesture = ''
        super().__init__()
        

    def choosing_gesture(self):
        gesture_index = input(f'Choose Your Gesture \nPress 0 for {self.gestures_list[0]}, \nPress 1 for {self.gestures_list[1]},\nPress 2 for {self.gestures_list[2]}, \nPress 3 for {self.gestures_list[3]}, \nPress 4 for {self.gestures_list[4]} \n ')
        if int(gesture_index) in range(5):
            self.gesture = self.gestures_list[int(gesture_index)]
            return self.gesture
      
        else:
            print(' Not a valid choice, try again...')
            
            return self.choosing_gesture()

     

          
        
     


