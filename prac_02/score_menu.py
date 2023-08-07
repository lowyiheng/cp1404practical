def main():
    score = get_valid_score()

    while True:

        print("\nMenu Options:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        option = input("Choose an option: ").upper()

        if option == "G":
            score = get_valid_score()
        elif option == "P":
            result = get_result(score)
            print("Result:", result)
        elif option == "S":
            print("Stars:")
            print_stars(score)
        elif option == "Q":
            print("Thank you for using the Score Menu. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    print("*" * score)

def get_valid_score():
    score = int(input("Enter a valid score (0-100 inclusive): "))
    while score < 0 or score > 100 :
        print("Invalid input. Score must be between 0 and 100.")
        score = int(input("Enter a valid score (0-100 inclusive): "))
    else:
        return score


if __name__ == "__main__":
    main()
