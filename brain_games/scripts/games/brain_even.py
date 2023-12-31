#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import play_game


def generate_even_question():
    number = random.randint(1, 100)
    print(f"Question: {number}")
    return number


def is_even(number):
    return number % 2 == 0


def get_even_correct_answer(question):
    return 'yes' if is_even(question) else 'no'


def check_even_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    play_game(
        "Answer 'yes' if the number is even, otherwise answer 'no'.",
        generate_even_question,
        get_even_correct_answer,
        check_even_answer
    )


if __name__ == "__main__":
    main()
