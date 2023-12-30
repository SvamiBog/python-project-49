#!/usr/bin/env python3

import random

def main():
    print("Welcome to the Brain Games!")
    play_even_game()


def welcome_user():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_question():
    return random.randint(1,100)


def is_even(number):
    return number % 2 == 0

def play_even_game():
    correct_answers_needed = 3
    correct_answers = 0
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    while correct_answers < correct_answers_needed:
        number = generate_question()
        print(f"Question: {number}")
        user_answer = input("Your answer: ").lower()

        if (is_even(number) and user_answer == 'yes') or (not is_even(number) and user_answer == 'no'):
            print("Correct!")
            correct_answers += 1
        else:
            correct_answer = 'yes' if is_even(number) else 'no'
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers == correct_answers_needed:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()