import random

def main():
    user_score = float(input("Enter your score: "))
    result = get_result(user_score)
    print("Your result is:", result)

    random_score = random.randint(0, 100)
    result = get_result(random_score)
    print("Random score:", random_score)
    print("Result for random score:", result)

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
