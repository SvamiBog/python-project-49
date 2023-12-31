#!/usr/bin/env python3

import random
from brain_games.scripts.game_logic import play_game


def generate_calc_question():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    print(f"Question: {question}")
    return question


def get_calc_correct_answer(question):
    return str(eval(question))


def check_calc_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    play_game(
        "What is the result of the expression?",
        generate_calc_question,
        get_calc_correct_answer,
        check_calc_answer
    )


if __name__ == "__main__":
    main()
