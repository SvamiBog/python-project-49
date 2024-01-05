#!/usr/bin/env python3

import random


INSTRUCTION_MESSAGE = "Find the greatest common divisor of given numbers."


def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    question = f"{num1} {num2}"
    return question, str(get_correct_answer(num1, num2))


def get_correct_answer(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
