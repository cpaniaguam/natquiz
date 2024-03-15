#!/usr/bin/env python3
import argparse
from ast import arg
import os
import platform
import random
from collections import Counter
from typing import List, Dict, Union

from natquiz.parse_questions import load_questions, show_questions


def select_questions(n:int) -> Dict[str, List[Dict[str, Union[int, str, List[str]]]]]:
    """
    Select `n` questions to ask during the quiz.

    Returns:
        Dict[str, List[Dict[str, Union[int, str, List[str]]]]]: A dictionary where each key is a string (the category) 
        and each value is a list of dictionaries. Each dictionary represents a question and contains three keys: 'id' (an integer), 
        'question' (a string), and 'answers' (a list of strings).

    Example:
        {
            'Principles of American Democracy': [
                {
                    'id': 1, 
                    'question': 'What is the supreme law of the land?', 
                    'answers': ['the Constitution']
                }, 
                {
                    'id': 5, 
                    'question': 'What do we call the first ten amendments to the Constitution?', 
                    'answers': ['the Bill of Rights']
                }
            ]
        }
    """

    questions:dict = load_questions()
    categories = list(questions.keys())
    # categories are
    # 'Principles of American Democracy'
    # 'System of Government'
    # 'Rights and Responsibilities'
    # 'American History'
    # 'Integrated Civics'

    # choose n categories
    selected_categories = Counter(random.choices(categories, k=n)) # sample with replacement
    questions_to_ask = {category: random.sample(questions[category], count) for category, count in selected_categories.items()}
    
    # Flatten questions_to_ask and shuffle
    questions_to_ask = [(cat, question) for cat, questions in questions_to_ask.items() for question in questions]
    random.shuffle(questions_to_ask)

    return questions_to_ask

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def ask_questions(n, clear_scr=True):
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

        # Pause between answer and next question
        if j < n:
            input("\n(Press enter for the next question)")
            if clear_scr:
                clear_screen()
        else:
            print("\nThis is the end of the quiz. Would you like to do another quiz? (Yes/No): ")
    
        print()


def bounded_int(x, low=1, high=10):
    try:
        x = int(x)
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid value: '{}'. Please provide an integer from 1 to 10.".format(x))
    if x < low or x > high:
        raise argparse.ArgumentTypeError("Number must be between 1 and 10")
    return x

def main():
    parser = argparse.ArgumentParser(description="natquiz - a US naturalization quiz app")
    parser.add_argument("-n", type=bounded_int, default=10, help="Number of questions to ask (default: 10)")
    parser.add_argument("--show-all", action="store_true", default=False, help="Show all questions and exit")
    parser.add_argument("--clear-scr", action="store_true", default=False, help="Clear screen after answer is shown (default: False unless specified)")
    args = parser.parse_args()

    if args.show_all:
        show_questions()
        return

    do_another = True
    while do_another:
        clear_screen()
        print(f"\n- US Naturalization Quiz -")
        print(f"\nNumber of questions to ask: {args.n}\n")
        ask_questions(args.n, clear_scr=args.clear_scr)

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
