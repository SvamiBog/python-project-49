#!/usr/bin/env python3

import random


RULE = "Find the greatest common divisor of given numbers."

MIN_NUMBER = 1
MAX_NUMBER = 50


def generate_question_and_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{num1} {num2}"
    return question, str(get_correct_answer(num1, num2))


def get_correct_answer(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
