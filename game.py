
from ai_player import Ai_player
from human_player import Human
import sys,time

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
        self.delprint('Welcome!\n')
        print()
        self.delprint('Each player picks from rock, paper, scissors, lizard or Spock\n')
        print()
        self.delprint(' Rock crushes Scissors \n Scissors cuts Paper  \n Paper covers Rock \n Rock crushes Lizard  \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard  \n Lizard eats Paper  \n Paper disproves Spock  \n Spock vaporizes Rock')
        print()
        self.delprint('\n First to TWO WINS or best of three wins is the OVERALL WINNER!!')
        print()



    
    
    def choosing_the_players(self):
        self.number_of_players = input(f' Choose the number of players from 0-2:  ')
        if self.number_of_players == '0':
            self.player_one = Ai_player()
            self.player_two = Ai_player() 
            self.delprint(' You have chosen AI vs AI') 
  
        elif self.number_of_players == '1':
            self.player_one = Human()
            self.player_two = Ai_player() 
            self.delprint(' You have chosen Human vs AI') 

        elif self.number_of_players == '2':
            self.player_one = Human()
            self.player_two = Human() 
            self.delprint(' You have chosen Human vs Human') 

        else:   
            self.delprint(' Can only be 0, 1 or 2 players...  Try again')
            self.choosing_the_players()


    
    def end_game_loop(self):
        while self.player_one_wins < 2 and self.player_two_wins < 2:
            print()
            self.collecting_gestures()
            self.compare_choices()
            print()
        if self.player_one_wins == 2:
            self.delprint('*****   Player One is Overall Winner   *****')
        elif self.player_two_wins == 2:
            self.delprint('*****   Player Two is Overall Winner    *****')
        print()



    def collecting_gestures(self):
        self.player_one_gesture = self.player_one.choosing_gesture()
        self.player_two_gesture = self.player_two.choosing_gesture()
        print()
        self.delprint(f'Player ONE has chosen {self.player_one_gesture}')
        self.delprint(f'Player TWO has chosen {self.player_two_gesture}')
    

    
    def compare_choices(self):
        if self.player_one_gesture == 'rock':
            if self.player_two_gesture == 'rock':
                self.delprint('tie')
            elif self.player_two_gesture == 'scissors' or 'lizard':

                self.delprint('Player 1 beats Player 2')
                self.player_one_wins += 1

            else:
                self.delprint('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'paper':
            if self.player_two_gesture == 'paper':
                self.delprint('tie')
            elif self.player_two_gesture == 'rock' or 'spock':
                self.delprint('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                self.delprint('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'scissors':
            if self.player_two_gesture == 'scissors':
                self.delprint('tie')
            elif self.player_two_gesture == 'paper' or self.player_two_gesture =='lizard':
                self.delprint('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                self.delprint('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'lizard':
            if self.player_two_gesture == 'lizard':
                self.delprint('tie')
            elif self.player_two_gesture == 'spock' or self.player_two_gesture =='paper':
                self.delprint('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                self.delprint('Player 2 beats Player 1')
                self.player_two_wins += 1
        elif self.player_one_gesture == 'spock':
            if self.player_two_gesture == 'spock':
                self.delprint('tie')
            elif self.player_two_gesture == 'scissors' or self.player_two_gesture =='rock':
                self.delprint('Player 1 beats Player 2')
                self.player_one_wins += 1
            else:
                self.delprint('Player 2 beats Player 1')
                self.player_two_wins += 1
        print()
        self.delprint(f'Total Player One Wins: {self.player_one_wins}')
        self.delprint(f'Total Player Two Wins: {self.player_two_wins}')

  

    def delprint(self,text): 
        for character in text + '\n':      
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(.05)
        


        


        
