#!/usr/bin/env python3

import random


INSTRUCTION_MESSAGE = "What number is missing in the progression?"


def generate_question():
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
    progression_as_strings = [str(item) for item in progression_list]
    progression_string = ' '.join(progression_as_strings)
    return progression_string, get_correct_answer(question)


def get_correct_answer(question):
    return question
