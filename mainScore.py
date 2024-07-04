from flask import Flask, render_template_string
import os

app = Flask(__name__)
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

@app.route('/')
def score_server():
    try:

        if os.path.exists(SCORES_FILE_NAME):
           with open(SCORES_FILE_NAME, 'r') as score_file:
               score = score_file.read().strip()
               score = int(score)  # Ensure the score is a number
        else:
            score = '0'
    except (FileNotFoundError, ValueError):
        return render_template_string("""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">Error reading the score</div></h1>
        </body>
        </html>
        """)

    return render_template_string(f"""
    <html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <h1>The score is <div id="score">{score}</div></h1>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
