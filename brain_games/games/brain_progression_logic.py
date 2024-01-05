#!/usr/bin/env python3

import random

INSTRUCTION_MESSAGE = "What number is missing in the progression?"


def generate_question():
    length = random.randint(5, 10)
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = generate_progression(start, step, length)
    hidden_element_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_element_index]
    progression_string = create_progression_string(
        progression, hidden_element_index
    )
    return progression_string, str(correct_answer)


def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def create_progression_string(progression, hidden_index):
    progression_with_hidden = progression[:]
    progression_with_hidden[hidden_index] = '..'
    return ' '.join(map(str, progression_with_hidden))
