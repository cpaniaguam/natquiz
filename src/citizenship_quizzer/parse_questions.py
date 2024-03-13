import tomllib

# Load the TOML file
with open('questions.toml', 'rb') as file:
    doc = tomllib.load(file)

# Access data
for question in doc['questions']:
    print(f"Category: {question['category']}")
    for q in question['questions']:
        print(f"Question ID: {q['id']}")
        print(f"Question: {q['question']}")
        print(f"Answers: {q['answers']}")
    print("\n")

# if __name__ == '__main__':
#     questions = parse_questions()
#     print(questions)