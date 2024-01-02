#!/usr/bin/env python3

import random


INSTRUCTION_MESSAGE = "Answer \"yes\" if given number is prime. "\
                            "Otherwise answer \"no\"."


def generate_question():
    question = random.randint(1, 100)
    return question, get_correct_answer(question)


def get_correct_answer(question):
    if question <= 1:
        return 'no'
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return 'no'
    return 'yes'
