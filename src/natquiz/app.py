#!/usr/bin/env python3
import argparse
import random

from natquiz.parse_questions import load_questions, show_questions


def select_questions(n):
    questions = load_questions()
    categories = list(questions.keys())

    # choose n categories
    selected_categories = random.choices(categories, k=n)
    questions_to_ask = []
    for category in selected_categories:
        # ensure unique questions are asked
        while True:
            _question = random.sample(questions[category], 1)[0]
            if _question not in questions_to_ask:
                questions_to_ask.append((category, _question))
                break
    return questions_to_ask


def ask_questions(n):
    questions_to_ask = select_questions(n)
    for j, (cat, _question) in enumerate(questions_to_ask, 1):
        id, question, answers = (
            _question["id"],
            _question["question"],
            _question["answers"],
        )
        print(f"Question {j} of {n}" f"\nCategory: {cat}" f"\n{question}")
        input("(Press enter to show answers)")
        for i, answer in enumerate(answers, 1):
            print(f"\tAnswer {i}: {answer}")
        print()


def main():
    parser = argparse.ArgumentParser(description="natquiz - a US naturalization quiz")
    parser.add_argument("-n", type=int, default=10, help="Number of questions to ask (default: 10)")
    parser.add_argument("--show-all", action="store_true", default=False, help="Show all questions and exit")
    args = parser.parse_args()

    if args.show_all:
        show_questions()
        return

    do_another = True
    while do_another:

        print(f"\n- US Naturalization Quiz -")
        print(f"\nNumber of questions to ask: {args.n}\n")
        ask_questions(args.n)
        print(
            "\nThis is the end of the quiz. Would you like to do another quiz? (Yes/No): "
        )

        while True:
            response = input()
            if not response or response.lower()[0] not in ["y", "n"]:
                print("Invalid input. Please enter Yes or No.")
            else:
                response = response.lower()[0]
                do_another = True if response == "y" else False
                break

    print("Good luck on your interview!\n")


if __name__ == "__main__":
    main()
