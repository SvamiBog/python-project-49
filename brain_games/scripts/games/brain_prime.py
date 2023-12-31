#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import play_game


def generate_prime_question():
    number = random.randint(1, 100)
    print(f"Question: {number}")
    return number


def get_prime_correct_answer(question):
    if question <= 1:
        return 'no'
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return 'no'
    return 'yes'


def check_prime_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    play_game(
        "Answer 'yes' if the number is even, otherwise answer 'no'.",
        generate_prime_question,
        get_prime_correct_answer,
        check_prime_answer
    )


if __name__ == "__main__":
    main()
