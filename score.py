import os

SCORES_FILE_NAME = "Scores.txt"
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    score = POINTS_OF_WINNING(difficulty)
    
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                current_score = int(file.read())
        else:
            current_score = 0

        new_score = current_score + score

        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))
    except Exception as e:
        print(f"An error occurred: {e}")
