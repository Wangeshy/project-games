from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyGame
from memoryGame import MemoryGame
from score import add_score
from utility import screen_cleaner


def welcome(name):
    print('Hello',name,'and welcome to the World of Games(WoG),\nHere you can find many cool games to play')

welcome(str(input('Please input your name')))



def load_game():
    while True:
        difficulty = input('Choose the level of difficulty: ')
        try:
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:

                break  # Exit the loop if a valid difficulty is entered
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    while True:
        n = (input('Choose the game to play:'))
        try:
             n = int(n)
             game_modules = {
                 1:MemoryGame(difficulty),
                 2: GuessGame(difficulty),
                 3: CurrencyGame(difficulty) }


             if n in game_modules:
                 game_module = game_modules[n]
                 user_won = game_module.play()

                 if user_won:
                    add_score(difficulty)
                    screen_cleaner()

                
                 break
             else:
                 print("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError:
                 print("Invalid input. Please enter a valid integer.")
    
    user_won = True  # This should be determined by the game logic
   
    



load_game()
