#!/usr/bin/env python3

import random
from brain_games.scripts.game_logic import play_game


def generate_gcd_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    print(f"Question: {num1} {num2}")
    return num1, num2


def check_gcd_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def get_gcd_correct_answer(question):
    num1, num2 = question
    while num2:
        num1, num2 = num2, num1 % num2
    return str(num1)


def main():
    play_game(
        "Find the greatest common divisor of given numbers.",
        generate_gcd_question,
        get_gcd_correct_answer,
        check_gcd_answer
    )


if __name__ == "__main__":
    main()
