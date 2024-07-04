import random
import time
from Game_Super import Game

class MemoryGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.user_won = False

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self, user_input=None):
        print("Welcome to the Memory Game!")
        print("You will be shown a sequence of numbers for 0.7 seconds.")
        print("Try to remember them and enter the same sequence afterward.")
        generated_sequence = self.generate_sequence()
        print(generated_sequence, end='', flush=True)  # Print without newline and flush the buffer
        time.sleep(0.9)
        print('\r' + ' ' * len(generated_sequence) + '\r', end='', flush=True)  # Overwrite the printed text

        if user_input is None:
            user_sequence = self.get_list_from_user()
        else:
            user_sequence = [int(x) for x in user_input.split(',')]

        print("Your sequence:", user_sequence)
        print("Generated sequence:", generated_sequence)
        if self.is_list_equal(user_sequence, generated_sequence):
            print("Congratulations! You won!")
            self.user_won = True
        else:
            print("Sorry, you lost. Better luck next time!")
            self.user_won = False

        return self.user_won

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        print("Now enter the numbers you remember:")
        user_sequence = []
        for _ in range(self.difficulty):
            while True:
                try:
                    number = int(input("Enter a number: "))
                    if 1 <= number <= 101:
                        user_sequence.append(number)
                        break
                    else:
                        print("Please enter a number between 1 and 101.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        return user_sequence

def main():
    while True:
        difficulty = input('Choose the level of difficulty: ')
        try:
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                game = MemoryGame(difficulty)
                game.play()
                break  # Exit the loop if a valid difficulty is entered
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
