#!/usr/bin/env python3

def play_game(welcome_message, generate_question,
              get_correct_answer, check_answer):
    correct_answers = 0
    correct_answers_needed = 3
    name = welcome_user()
    print(f"{welcome_message}")

    while correct_answers < correct_answers_needed:
        question = generate_question()
        user_answer = input("Your answer: ").lower()
        correct_answer = get_correct_answer(question)

        if check_answer(user_answer, correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers == correct_answers_needed:
        print(f"Congratulations, {name}!")


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def main():
    print('hello world!')


if __name__ == "__main__":
    main()
