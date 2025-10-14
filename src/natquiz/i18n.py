#!/usr/bin/env python3
"""Internationalization (i18n) module for natquiz."""

# UI strings for English
STRINGS_EN = {
    "title": "US Naturalization Quiz",
    "num_questions": "Number of questions to ask: {}",
    "question_header": "Question {} of {}",
    "category": "Category: {}",
    "press_enter_show_answers": "(Press enter to show answers)",
    "answer_prefix": "Answer {}: {}",
    "press_enter_next": "(Press enter for the next question)",
    "end_quiz": "\nThis is the end of the quiz. Would you like to do another quiz? (Yes/No): ",
    "invalid_input": "Invalid input. Please enter Yes or No.",
    "good_luck": "Good luck on your interview!",
    "section": "Section: {}",
}

# UI strings for Spanish
STRINGS_ES = {
    "title": "Examen de Naturalización de los Estados Unidos",
    "num_questions": "Número de preguntas: {}",
    "question_header": "Pregunta {} de {}",
    "category": "Categoría: {}",
    "press_enter_show_answers": "(Presione enter para mostrar las respuestas)",
    "answer_prefix": "Respuesta {}: {}",
    "press_enter_next": "(Presione enter para la siguiente pregunta)",
    "end_quiz": "\nEste es el final del examen. ¿Le gustaría hacer otro examen? (Sí/No): ",
    "invalid_input": "Entrada inválida. Por favor ingrese Sí o No.",
    "good_luck": "¡Buena suerte en su entrevista!",
    "section": "Sección: {}",
}

# Mapping of language codes to string dictionaries
LANGUAGES = {
    "en": STRINGS_EN,
    "es": STRINGS_ES,
}

def get_strings(language="en"):
    """
    Get UI strings for the specified language.
    
    Args:
        language: Language code (e.g., "en", "es")
    
    Returns:
        Dictionary of UI strings
    """
    return LANGUAGES.get(language, STRINGS_EN)
