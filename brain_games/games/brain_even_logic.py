#!/usr/bin/env python3

import random


INSTRUCTION_MESSAGE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def generate_question():
    question = random.randint(1, 100)
    return question, get_correct_answer(question)


def is_even(number):
    return number % 2 == 0


def get_correct_answer(question):
    return 'yes' if is_even(question) else 'no'
