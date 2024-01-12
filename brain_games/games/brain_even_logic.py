#!/usr/bin/env python3

import random


RULE = "Answer \"yes\" if the number is even, "\
       "otherwise answer \"no\"."

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question_and_answer():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    return question, get_correct_answer(question)


def is_even(number):
    return number % 2 == 0


def get_correct_answer(question):
    return 'yes' if is_even(question) else 'no'
