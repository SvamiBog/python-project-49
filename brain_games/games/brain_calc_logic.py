#!/usr/bin/env python3

import random


INSTRUCTION_MESSAGE = "What is the result of the expression?"


def generate_question():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    return question, get_correct_answer(question)


def get_correct_answer(question):
    return str(eval(question))
