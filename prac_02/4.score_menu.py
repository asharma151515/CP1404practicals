import random

def main_menu():
    score = 0
    choice = ''
    while choice != 'Q':
        print("Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell")
        else:
            print("Invalid input. Please try again.")

def determine_result(score):
    """Determine the result based on the score"""
    if score >= 0 and score <= 50:
        return "Fail"
    elif score > 50 and score <= 65:
        return "Pass"
    elif score > 65 and score <= 75:
        return "Credit"
    elif score > 75 and score <= 85:
        return "Distinction"
    elif score > 85 and score <= 100:
        return "High Distinction"
    else:
        return "Invalid score"

def get_valid_score():
    score = int(input("Enter a valid score (0-100 inclusive): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = int(input("Enter a valid score (0-100 inclusive): "))
    return score

def print_result(score):
    result = determine_result(score)
    print("Result:", result)

def show_stars(score):
    print("*" * score)

if __name__ == "__main__":
    main_menu()