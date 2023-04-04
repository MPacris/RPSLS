# RPSLS
group activity

Setup Steps
Create a GitHub repository on GitHub. Remember to use a Python .gitignore and add a README! -done

Clone your repository down to your computer (referring to the Code Demo – Source Control video would be helpful here!) -done

Create your project in Visual Studio Code and move the invisible .git folder and README file to the folder where your project is located.-done

Make a test commit and check your repository to be sure the content has been updated!-done

In the project, add the debugger for Python in Visual Studio Code 

Create a main.py file to serve as the entry point for your application when you run it -created

Start creating classes. Start thinking through what every class “has” and “does” based on the user stories and instructor discussion.

Before you begin coding, write an algorithm that represents the steps necessary to play a game of rock, paper, scissors, lizard, Spock in a best-of-three format. By 

writing out the steps, it will make you think about every piece needed to bring the 





STEPS


explain the rules
-rules will come out as a string

-each player will choose 1 of 5 'gestures'
  -gestures will come from a list or should come from a class
  
  

-each gesture can defeat another as defined:
  -rules what beats what:
    Rock crushes Scissors
    Scissors cuts Paper 
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock

  

define number of players

input - pick number of players:  This can be a list
  if 0 then : AI vs AI
  if 1 then : Person vs A
  if 2 then " Person vs Person
  if 3 the pick again


-choosing number of players can also be AI vs AI
-players will be the Class,  feeding off that would be person choice or random choice
-player will select a gesture from a list
  
  -person should be given choices from a list and will input the choice
  -AI- randomly select the chooses from the list
  

-outcome, player vs player input vs input or 1 player : input vs random or random vs random
-look at this at doing this as classes where player vs player;  or player vs AI; AI vs AI


run the game
  -list of gestures lives here
  
  -While loop runnning a counter  
     -counting player winse up to 2
      if wins  == 2 for either player then display_winner ()
        comparison of given gesture

  player one choice
    if player choice is ROCK and player 2 choice is scissors or lizard  
          print player one is winner
            Rock crushes Scissors
            Rock crushes Lizard
          elif Rock and player Rock 
            print this is a tie
          else:  player one loses
          
        will have one for each gesture that can me chosen
        
   -best two out of three to determine the winner

        


display winner
print OUTRO
  do you want to replay here and reset counter
  
  ####to handle discrepancies where there are choices, need to have a loop of sorts
  
  
  





