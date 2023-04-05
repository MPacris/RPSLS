
from ai_player import Ai_player
from human_player import Human

class Game:

    def __init__(self) -> None:
        self.player_one_gesture = ''
        self.player_two_gesture = ''
        self.player_one_wins = 0
        self.player_two_wins = 0
    
    def run_game(self):
        self.explaining_rules()
        self.choosing_the_players()
        self.end_game_loop()
    


    
    def explaining_rules(self):
        print('Welcome!')
        print()
        print('each player picks from rock, paper, scissors, lizard or Spock')
        print()
        print('Rock crushes Scissors \n Scissors cuts Paper  \n Paper covers Rock \n Rock crushes Lizard  \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard  \n Lizard eats Paper  \n Paper disproves Spock  \n Spock vaporizes Rock')
        print()
        print('First to TWO WINS or best of three wins is the OVERALL WINNER!!')
        print()



    
    
    def choosing_the_players(self):
        self.number_of_players = input(f'choose the number of players from 0-2-  ')
        if self.number_of_players == '0':
            self.player_one = Ai_player()
            self.player_two = Ai_player() 
            print('you have chosen AI vs AI') 
  
        elif self.number_of_players == '1':
            self.player_one = Human()
            self.player_two = Ai_player() 
            print('you have chosen Human vs AI') 

        elif self.number_of_players == '2':
            self.player_one = Human()
            self.player_two = Human() 
            print('you have chosen Human vs Human') 

        else:   
            print('Can only be 0, 1 or 2 players')
            self.choosing_the_players()


    
    def end_game_loop(self):
        while self.player_one_wins < 2 and self.player_two_wins < 2:
            self.collecting_gestures()
            self.compare_choices()
        if self.player_one_wins == 2:
            print('Player One is Overall Winner')
        elif self.player_two_wins == 2:
            print('Player Two is Overall Winner')
        print()



    def collecting_gestures(self):
        self.player_one_gesture = self.player_one.choosing_gesture()
        self.player_two_gesture = self.player_two.choosing_gesture()

        print(f'Player ONE has chosen {self.player_one_gesture}')
        print(f'Player TWO has chosen {self.player_two_gesture}')
    

    
    def compare_choices(self):
        if self.player_one_gesture == 'rock':
            if self.player_two_gesture == 'rock':
                print('tie')
            elif self.player_two_gesture == 'scissors' or 'lizard':
                print('Player 1 beats Player 2')
                self.player_one_wins += 1

            else:
                print('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'paper':
            if self.player_two_gesture == 'paper':
                print('tie')
            elif self.player_two_gesture == 'rock' or 'spock':
                print('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                print('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'scissors':
            if self.player_two_gesture == 'scissors':
                print('tie')
            elif self.player_two_gesture == 'paper' or self.player_two_gesture =='lizard':
                print('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                print('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'lizard':
            if self.player_two_gesture == 'lizard':
                print('tie')
            elif self.player_two_gesture == 'spock' or self.player_two_gesture =='paper':
                print('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                print('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'spock':
            if self.player_two_gesture == 'spock':
                print('tie')
            elif self.player_two_gesture == 'scissors' or self.player_two_gesture =='rock':
                print('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                print('Player 2 beats Player 1')
                self.player_two_wins += 1

        print(f'Total Player One Wins: {self.player_one_wins}')
        print(f'Total Player Two Wins: {self.player_two_wins}')

  
    

        


        


        
