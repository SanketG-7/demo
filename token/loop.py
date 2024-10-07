# Simple Quiz Application

def display_question(question, options):
    """Display a question and its options."""
    print(question)
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

def get_user_answer():
    """Get and validate user answer."""
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct."""
    return user_answer == correct_answer

def main():
    """Main function to run the quiz."""
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct": 2
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["Mark Twain", "Charles Dickens", "William Shakespeare", "Leo Tolstoy"],
            "correct": 3
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct": 4
        }
    ]

    score = 0

    print("Welcome to the Quiz!")
    print("---------------------")

    for q in questions:
        display_question(q["question"], q["options"])
        user_answer = get_user_answer()
        
        if check_answer(user_answer, q["correct"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['options'][q['correct'] - 1]}\n")

    print(f"Your final score is {score} out of {len(questions)}.")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
