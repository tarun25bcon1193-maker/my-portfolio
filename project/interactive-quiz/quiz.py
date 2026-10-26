questions = [
    {
        "question": "Which language is this program written in?",
        "options": ["A. Java", "B. Python", "C. HTML"],
        "answer": "B"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["A. print()", "B. input()", "C. scan()"],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean"],
        "answer": "C"
    }
]

score = 0

for item in questions:
    print("\n" + item["question"])

    for option in item["options"]:
        print(option)

    answer = input("Your answer (A/B/C): ").strip().upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"\nYour final score: {score}/{len(questions)}")