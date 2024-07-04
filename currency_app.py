from flask import Flask, render_template, request, jsonify
import random
import requests

app = Flask(__name__)

class CurrencyGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self):
        # Simulating API call to get exchange rate
        exchange_rate = random.uniform(3.5, 4.5)  # Random exchange rate for illustration
        t = random.randint(1, 100)
        lower_bound = t - (5 - self.difficulty)
        upper_bound = t + (5 - self.difficulty)
        return lower_bound * exchange_rate, upper_bound * exchange_rate

    def get_guess_from_user(self):
        try:
            guess = float(request.json['user_input'])
            return guess
        except (KeyError, ValueError):
            return None

    def play(self):
        try:
            user_input = request.json.get('user_input', '')

            if user_input == '':
                return jsonify({'result': 'Please enter a valid input.'}), 400

            user_guess = self.get_guess_from_user()
            if user_guess is None:
                return jsonify({'result': 'Invalid input. Please enter a valid number.'}), 400

            lower_bound, upper_bound = self.get_money_interval()

            if lower_bound <= user_guess <= upper_bound:
                return jsonify({'result': 'Congratulations! Your guess is correct.'})
            else:
                return jsonify({'result': 'Sorry, your guess is incorrect. The correct value was between the interval.'})

        except Exception as e:
            return jsonify({'result': f'An error occurred: {str(e)}'}), 500

@app.route('/play', methods=['POST'])
def play():
    try:
        data = request.json
        game_type = int(data['game'])
        difficulty = int(data['difficulty'])

        if game_type == 3:
            game = CurrencyGame(difficulty)
            return game.play()

        return jsonify({'result': 'Invalid game type selected.'}), 400

    except Exception as e:
        return jsonify({'result': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
