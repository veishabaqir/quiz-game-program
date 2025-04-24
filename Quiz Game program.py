# Python Quiz Game

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

    score = 0

    print("Welcome to the Quiz Game!")
    print("Answer the following questions by typing the letter of the correct option.\n")

    # Iterate through the questions
    for question, details in questions.items():
        print(question)
        for option in details["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()

        if answer == details["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {details['answer']}.\n")

    # Display the final score
    print(f"Quiz Over! Your final score is {score}/{len(questions)}.")

# Run the quiz game
if __name__ == "__main__":
    quiz_game()