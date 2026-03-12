#NAME:AL AMIN KABIR YAKASAI
#MATRIC N0: MAAUN/24/DTS/0002
# Mini CBT Quiz Engine

questions = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Ibadan"],
        "correct_answer": "B"
    },
    {
        "question": "Which language is commonly used in Data Science?",
        "options": ["A. HTML", "B. CSS", "C. Python", "D. Word"],
        "correct_answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Central Processing Unit",
            "C. Computer Personal Unit",
            "D. Control Process Utility"
        ],
        "correct_answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

def calculate_percentage(score, total):
    return (score / total) * 100

percentage = calculate_percentage(score, len(questions))

print("\nFinal Score:", score, "/", len(questions))
print("Percentage:", percentage, "%")

if percentage >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
