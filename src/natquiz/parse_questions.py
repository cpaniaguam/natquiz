#!/usr/bin/env python3
import tomllib
from pathlib import Path


def load_questions():
    path = Path(__file__).parent / "questions.toml"

    with open(path, "rb") as file:
        doc = tomllib.load(file)
    return doc


def show_questions():
    doc = load_questions()
    for section, questions in doc.items():
        print(f"Section: {section}")
        for question in questions:
            id = question["id"]
            _question = question["question"]
            answers = question["answers"]
            print(f"\nQuestion {id}: {_question}")
            for i, answer in enumerate(answers, 1):
                print(f"\tAnswer {i}: {answer}")


if __name__ == "__main__":
    show_questions()
