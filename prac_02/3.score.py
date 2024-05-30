import random


def main():
    user_score = int(input("Enter your score: "))
    result = determine_result(user_score)
    print("Result:", result)

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print("Random Score:", random_score)
    print("Random Result:", random_result)


def determine_result(score):
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


if __name__ == "__main__":
    main()
