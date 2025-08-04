from game_logics import number_generator, hint, scorer
from utils import input_validator
import time


def Game():
    actual_number = number_generator.GenerateNumber(1, 100)
    score = scorer.Scorer()

    playing = True
    while playing:
        user_guess = input_validator.get_valid_input("Enter your guess: ", 1, 100)
        if user_guess == actual_number:
            print(f"Congratulations! Your final score is: {score.get_score()}")
            time.sleep(2)
            while True:
                play_again = input("do you wan play again?(yes)(no) ")
                if play_again == 'yes' or play_again == 'y':
                    Game()
                elif play_again == 'no' or play_again == 'n':
                    print("Goodbye!")
                    playing = False
                    break
                else:
                    print("Invalid input!")
        else:
            print(hint.hint(guess=user_guess, actual_number=actual_number))
            score.decrement_score()



if __name__ == "__main__":
    Game() 
