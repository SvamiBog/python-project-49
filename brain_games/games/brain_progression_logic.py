#!/usr/bin/env python3

import random

RULE = "What number is missing in the progression?"

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_TERM = 1
MAX_TERM = 100
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10


def generate_question_and_answer():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    first_term = random.randint(MIN_TERM, MAX_TERM)
    difference = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    progression = generate_progression(first_term, difference, length)
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
