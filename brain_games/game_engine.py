#!/usr/bin/env python3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def play_game(game):
    correct_answers = 0
    CORRECT_ANSWERS_NEEDED = 3
    name = welcome_user()
    print(f"{game.INSTRUCTION_MESSAGE}")

    while correct_answers < CORRECT_ANSWERS_NEEDED:
        question, correct_answer = game.generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").lower()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers == CORRECT_ANSWERS_NEEDED:
        print(f"Congratulations, {name}!")
