import random

LENGTH = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks <= 0:
        print("Invalid input!")
        quick_picks = int(input("How many quick picks? "))

    for column in range(quick_picks):
        quick_pick = []
        for row in range(LENGTH):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
