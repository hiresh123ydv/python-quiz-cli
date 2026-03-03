import random
import time


def quiz_game():

    # ------------------ LOAD HIGH SCORE ------------------
    try:
        with open("high_score.txt", "r") as file:
            data = file.read().strip()
            if data:
                name, high_score = data.split(",")
                high_score = int(high_score)
            else:
                name = ""
                high_score = 0
    except FileNotFoundError:
        name = ""
        high_score = 0

    
    print("=" * 50)
    print("🎮 PYTHON QUIZ GAME 🎮".center(50))
    print("=" * 50)

    player_name = input("Enter your name: ")

    if high_score > 0:
        print(f"Current High Score: {high_score} by {name}")
    else:
        print("No high score yet. Be the first!")

    # ------------------ QUESTIONS ------------------
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Chennai", "B. New Delhi", "C. Kolkata", "D. Mumbai"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "Who is known as the Father of Computers?",
            "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "A"
        },
        {
            "question": "What is the largest ocean in the world?",
            "options": ["A. Indian Ocean", "B. Atlantic Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Which data structure works on LIFO principle?",
            "options": ["A. Queue", "B. Stack", "C. Array", "D. Linked List"],
            "answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "Which country is home to the Great Wall?",
            "options": ["A. India", "B. China", "C. Japan", "D. Korea"],
            "answer": "B"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Power Unit"],
            "answer": "B"
        }
    ]

    score = 0
    random.shuffle(questions)

    # ------------------ QUIZ LOOP ------------------
    for q in questions:

        print("\n" + "-" * 50)
        print(f"Question: {q['question']}")
        print("-" * 50)

        for option in q["options"]:
            print(option)

        # Start timer BEFORE input loop
        start_time = time.time()

        while True:
            try:
                user_input = input("Enter option (A/B/C/D): ").upper()
            except EOFError:
                print("\nInput interrupted. Exiting game.")
                return

            if user_input in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid option. Please enter A, B, C, or D.")

        end_time = time.time()
        time_taken = end_time - start_time

        # Check time limit
        if time_taken > 15:
            print(f"⏳ Time's up! You took {time_taken:.2f} seconds.")
            continue

        # Check answer
        if user_input == q["answer"]:
            score += 1
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            for option in q["options"]:
                if option.startswith(q["answer"]):
                    print(f"Correct answer is: {option}")
                    break

        print(f"You answered in {time_taken:.2f} seconds")

    # ------------------ RESULTS ------------------
    time.sleep(1)
    print("\nCalculating results...")
    time.sleep(1.5)

    print("-" * 50)
    print(f"Your final score is {score} out of {len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Your percentage is {percentage:.2f}%")

    if percentage == 100:
        print("🏆 Outstanding performance!")
    elif percentage >= 70:
        print("👍 Good job!")
    elif percentage >= 40:
        print("🙂 Not bad, keep practicing!")
    else:
        print("💪 You need more practice!")

    # ------------------ SAVE HIGH SCORE ------------------
    if score > high_score:
        print("🎉 New High Score!")
        with open("high_score.txt", "w") as file:
            file.write(f"{player_name},{score}")
    else:
        print(f"High Score remains: {high_score} by {name}")

    print("\n" + "=" * 50)
    print("🏁 QUIZ COMPLETED 🏁".center(50))
    print("=" * 50)



quiz_game()