def quiz_game():
    # Dictionary to store questions, options, and answers
    questions = {
        "What is the capital of France?": {
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "A"
        },
        "Which programming language is known as the 'language of the web'?": {
            "options": ["A. Python", "B. JavaScript", "C. Java", "D. C++"],
            "answer": "B"
        },
        "What is the largest planet in our solar system?": {
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "C"
        },
        "Who wrote 'To Kill a Mockingbird'?": {
            "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
            "answer": "A"
        },
        "What is the chemical symbol for water?": {
            "options": ["A. H2O", "B. O2", "C. CO2", "D. NaCl"],
            "answer": "A"
        }
    }

    print("🎉 Welcome to the Quiz Game! 🎉")
    name = input("Enter your name: ").strip()
    print(f"\nHi {name}! Answer the following questions by typing A, B, C, or D.\n")

    score = 0
    total_questions = len(questions)

    for idx, (question, details) in enumerate(questions.items(), start=1):
        print(f"Q{idx}: {question}")
        for option in details["options"]:
            print(option)

        # Input validation
        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("❌ Invalid input. Please enter A, B, C, or D.")

        # Check the answer
        if answer == details["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            correct_option = next(opt for opt in details["options"] if opt.startswith(details["answer"]))
            print(f"❌ Wrong! The correct answer was {correct_option}\n")

    # Final score summary
    percentage = (score / total_questions) * 100
    print(f"🏁 Quiz Over! {name}, your final score is {score}/{total_questions} ({percentage:.2f}%).")
    if percentage == 100:
        print("🎉 Perfect score! You're a quiz master!")
    elif percentage >= 60:
        print("👍 Great job!")
    else:
        print("📘 Keep practicing and you'll get there!")

# Run the quiz game
if __name__ == "__main__":
    quiz_game()
