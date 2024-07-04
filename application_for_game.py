from flask import Flask, render_template, request, jsonify
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyGame
from memoryGame import MemoryGame
from score import add_score
from utility import screen_cleaner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('gamecodehtml.html')

@app.route('/play', methods=['POST'])
def play():
    try:
        data = request.json
        game_type = int(data['game'])
        difficulty = int(data['difficulty'])
        user_input = data.get('user_input', '')

        if user_input == '':
            return jsonify({'result': 'Please enter a valid input.'}), 400

        # Initialize the appropriate game based on user input
        if game_type == 1:
            game = MemoryGame(difficulty)
        elif game_type == 2:
            game = GuessGame(difficulty)
        elif game_type == 3:
            game = CurrencyGame(difficulty)
        else:
            return jsonify({'result': 'Invalid game type selected'})

        # Play the game
        user_won = game.play(user_input)

        # Update score and clean screen if the user won
        if user_won:
            add_score(difficulty)
            screen_cleaner()

        return jsonify({'result': 'You won!' if user_won else 'You lost!'})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'result': 'An error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=True)
