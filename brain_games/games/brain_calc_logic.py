#!/usr/bin/env python3

import random


RULE = "What is the result of the expression?"

MIN_NUMBER = 1
MAX_NUMBER = 25


def generate_question_and_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    return question, get_correct_answer(question)


def get_correct_answer(question):
    return str(eval(question))
