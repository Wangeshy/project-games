import random
from Game_Super import Game

class GuessGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.secret_number = None
        self.user_won = False

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Please enter a number between 1 and {self.difficulty}.")
                    
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, guess):
        if guess == self.secret_number:
            print("Congratulations! You guessed the correct number!")
            self.user_won = True
        elif guess < self.secret_number:
            print("The secret number is higher.")
        else:
            print("The secret number is lower.")
            self.user_won = False

        return self.user_won

    def play(self, user_input=None):
        self.generate_number()
        while True:
            if user_input is None:
              user_guess = self.get_guess_from_user()
            else:
              user_guess = int(user_input)
        
            if self.compare_results(user_guess):
              return True
           

def main():
    while True:
        difficulty = input('Choose the level of difficulty: ')
        try:
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                game = GuessGame(difficulty)
                game.play()
                break  # Exit the loop if a valid difficulty is entered
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
