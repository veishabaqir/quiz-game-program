import random

def quiz_game():
    questions = {
        "What is the capital of France?": {
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        "Which programming language is known as the 'language of the web'?": {
            "options": ["Python", "JavaScript", "Java", "C++"],
            "answer": "JavaScript"
        },
        "What is the largest planet in our solar system?": {
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Jupiter"
        },
        "Who wrote 'To Kill a Mockingbird'?": {
            "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"],
            "answer": "Harper Lee"
        },
        "What is the chemical symbol for water?": {
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "H2O"
        }
    }

    def play():
        print("🎉 Welcome to the Quiz Game! 🎉")
        name = input("Enter your name: ").strip()
        print(f"\nHi {name}! Answer the following questions by typing A, B, C, or D.\n")

        score = 0
        total_questions = len(questions)
        question_items = random.sample(list(questions.items()), total_questions)

        for idx, (question, details) in enumerate(question_items, start=1):
            print("➖" * 50)
            print(f"Q{idx}: {question}")

            options = random.sample(details["options"], len(details["options"]))  # Shuffle options
            option_map = {chr(65+i): option for i, option in enumerate(options)}  # Map A, B, C, D

            for key, val in option_map.items():
                print(f"{key}. {val}")

            while True:
                answer = input("Your answer (A/B/C/D): ").strip().upper()
                if answer in option_map:
                    break
                else:
                    print("❌ Invalid input. Please enter A, B, C, or D.")

            if option_map[answer] == details["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                correct_letter = next(k for k, v in option_map.items() if v == details["answer"])
                print(f"❌ Wrong! The correct answer was {correct_letter}. {details['answer']}\n")

        percentage = (score / total_questions) * 100
        print("➖" * 50)
        print(f"🏁 Quiz Over! {name}, your final score is {score}/{total_questions} ({percentage:.2f}%).")

        if percentage == 100:
            print("🌟 Perfect score! You're a quiz master!")
        elif percentage >= 60:
            print("👏 Great job!")
        else:
            print("📘 Keep practicing and you'll improve!")

    # Allow user to replay
    while True:
        play()
        retry = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("👋 Thanks for playing! Goodbye.")
            break

# Run the quiz game
if __name__ == "__main__":
    quiz_game()

