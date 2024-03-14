#!/usr/bin/env python3
import argparse

from citizenship_quizzer.parse_questions import show_questions

# TODO
def main():
    parser = argparse.ArgumentParser(description='Citizenship Quizzer')
    parser.add_argument('-n', type=int, help='Number of questions to ask')
    args = parser.parse_args()

    print(f"Number of questions to ask: {args.n}")

    print(f"For now, here are all the questions:")
    show_questions()

if __name__ == '__main__':
    main()