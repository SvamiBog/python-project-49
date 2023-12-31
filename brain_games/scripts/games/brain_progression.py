#!/usr/bin/env python3

import random
from brain_games.scripts.brain_games import play_game


def generate_progression_question():
    length = random.randint(5, 10)
    first_num = random.randint(1, 100)
    progression_num = random.randint(1, 50)
    progression_list = []

    for i in range(length):
        current_number = first_num + progression_num * i
        progression_list.append(current_number)

    question_num = random.randint(0, length - 1)
    question = f"{progression_list[question_num]}"
    progression_list[question_num] = '..'
    print(f"Question: {progression_list}")
    return question


def get_progression_correct_answer(question):
    return question


def check_progression_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    play_game(
        "What number is missing in the progression?",
        generate_progression_question,
        get_progression_correct_answer,
        check_progression_answer
    )


if __name__ == "__main__":
    main()
