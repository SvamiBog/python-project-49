#!/usr/bin/env python3

import random


RULE = "Answer \"yes\" if given number is prime. "\
       "Otherwise answer \"no\"."

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question_and_answer():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    return question, get_correct_answer(question)


def get_correct_answer(question):
    return 'yes' if is_prime(question) else 'no'


def is_prime(question):
    if question <= 1:
        return False
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return False
    return True
