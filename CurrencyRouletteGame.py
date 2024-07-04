import random
import requests
from Game_Super import Game

class CurrencyGame(Game):
    def __init__(self, difficulty):
        super().__init__(difficulty)

    def get_money_interval(self):
        # Get the current exchange rate from USD to ILS using the currency API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        exchange_rate = data["rates"]["ILS"]

        # Generate an interval based on difficulty and exchange rate
        t = random.randint(1, 100)
        lower_bound = t - (5 - self.difficulty)
        upper_bound = t + (5 - self.difficulty)
        return lower_bound * exchange_rate, upper_bound * exchange_rate

    def get_guess_from_user(self):
        while True:
            try:
                guess = float(input("Enter your guess for the value in ILS: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self, user_input=None):
        print("Welcome to the Currency Game!")
        lower_bound, upper_bound = self.get_money_interval()
        print(f"Guess the value of the generated number in ILS. It's between {lower_bound} and {upper_bound}.")

        if user_input is None or user_input.strip() == '':
            user_guess = self.get_guess_from_user()
        else:
            try:
                user_guess = float(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return False

        if lower_bound <= user_guess <= upper_bound:
            print("Congratulations! Your guess is correct.")
            return True
        else:
            print("Sorry, your guess is incorrect. The correct value was between the interval.")
            return False

def main():
    difficulty = int(input("Enter the difficulty level (1-5): "))
    game = CurrencyGame(difficulty)
    game.play()

if __name__ == "__main__":
    main()
