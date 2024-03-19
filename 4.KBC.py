import random
questions = [
    ("Who is the Prime Minister of India", "Narendra Modi"),
    ("Who is the Chief Minister of Maharashtra?", "Eknath Shinde"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What is the chemical symbol for water?", "H2O")
]
def play_game():
    total_amount = 0
    for i, (question, answer) in enumerate(questions, start=1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            total_amount += 1000  # Incrementing the amount by 1000 for each correct answer
        else:
            print("Incorrect!")
            break  # End the game if the user answers incorrectly
    return total_amount

# Main function to run the game
def main():
    print("Welcome to KBC (Kaun Banega Crorepati)!")
    print("Answer the following questions to win money.")
    print("You will earn Rs. 1000 for each correct answer.")
    print("You can quit at any time by answering incorrectly.")
    print("Let's get started!\n")
    
    total_amount = play_game()
    
    print(f"\nCongratulations! You are taking home Rs. {total_amount}.")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
