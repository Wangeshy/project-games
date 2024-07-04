from flask import Flask, render_template, request, jsonify
import random
import requests

app = Flask(__name__)

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.user_won = False

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self, user_input=None):
        
        generated_sequence = self.generate_sequence()
        if user_input is None:
            return jsonify({'sequence': generated_sequence})
        else:
            user_sequence = [int(x) for x in user_input.split(',')]
            if self.is_list_equal(user_sequence, generated_sequence):
                self.user_won = True
                return jsonify({'result': 'Congratulations! You won!'})
            else:
                self.user_won = False
                return jsonify({'result': 'Sorry, you lost. Better luck next time!'})

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        return []

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None
        self.user_won = False

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def play(self, user_input=None):
        self.generate_number()
        try:
            user_guess = int(user_input)
            if user_guess == self.secret_number:
                return jsonify({'result': 'Congratulations! You guessed the correct number!'})
            elif user_guess < self.secret_number:
                return jsonify({'result': 'The secret number is higher.'})
            else:
                return jsonify({'result': 'The secret number is lower.'})
        except ValueError:
            return jsonify({'result': 'Invalid input. Please enter a valid number.'}), 400

class CurrencyGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self):
        # Dummy exchange rate for this example
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        exchange_rate = data["rates"]["ILS"]
        t = random.randint(1, 100)
        lower_bound = t - (5 - self.difficulty)
        upper_bound = t + (5 - self.difficulty)
        return lower_bound * exchange_rate, upper_bound * exchange_rate

    def play(self, user_input=None):
        lower_bound, upper_bound = self.get_money_interval()
        try:
            user_guess = float(user_input)
            if lower_bound <= user_guess <= upper_bound:
                return jsonify({'result': 'Congratulations! Your guess is correct.'})
            else:
                return jsonify({'result': 'Sorry, your guess is incorrect. The correct value was between the interval.'})
        except ValueError:
            return jsonify({'result': 'Invalid input. Please enter a valid number.'}), 400

@app.route('/')
def index():
    return render_template('gamecodehtml2.html')

@app.route('/play', methods=['POST'])
def play():
    try:
        data = request.json
        game_type = int(data['game'])
        difficulty = int(data['difficulty'])
        user_input = data['user_input']

        if game_type == 1:
            game = MemoryGame(difficulty)
            return game.play(user_input)
        elif game_type == 2:
            game = GuessGame(difficulty)
            return game.play(user_input)
        elif game_type == 3:
            game = CurrencyGame(difficulty)
            return game.play(user_input)

        return jsonify({'result': 'Invalid game type selected.'}), 400

    except Exception as e:
        return jsonify({'result': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
