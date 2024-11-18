import random
from time import sleep as sl

from questions import questions


def main():
    question_list = list(questions.items())
    random.shuffle(question_list)

    score = 0

    while True:
        for question, answer in question_list:
            print(question)
            sl(0.4)
            user_answer = input("Your answer (input Q to exit): \n- ")

            if user_answer.lower() == answer.lower():
                print("This is correct :) \n")
                score += 1
            elif user_answer.lower() == "q":
                print(f"Your score: {score} points out of {len(question_list)} ")
                print("Exiting, goodbye \n")
                return
            else:
                print("Incorrect :( \n")

    print(f"Your score: {score} points out of {len(question_list)} ")


if __name__ == "__main__":
    main()
