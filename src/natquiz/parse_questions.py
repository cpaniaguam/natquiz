#!/usr/bin/env python3
import tomllib
from pathlib import Path
from natquiz.i18n import get_strings


def load_questions(language="en"):
    """
    Load questions from the appropriate language file.
    
    Args:
        language: Language code (e.g., "en", "es")
    
    Returns:
        Dictionary of questions organized by category
    """
    if language == "es":
        path = Path(__file__).parent / "questions_es.toml"
    else:
        path = Path(__file__).parent / "questions.toml"

    with open(path, "rb") as file:
        doc = tomllib.load(file)
    return doc


def show_questions(language="en"):
    """
    Display all questions in the specified language.
    
    Args:
        language: Language code (e.g., "en", "es")
    """
    doc = load_questions(language)
    strings = get_strings(language)
    for section, questions in doc.items():
        print(strings["section"].format(section))
        for question in questions:
            id = question["id"]
            _question = question["question"]
            answers = question["answers"]
            print(f"\nQuestion {id}: {_question}")
            for i, answer in enumerate(answers, 1):
                print(f"\tAnswer {i}: {answer}")


if __name__ == "__main__":
    show_questions()
