MINIMUM_PASSWORD = 0
def main():
    password = get_password()
    asterisks(password)


def get_password():
    password = input("Please enter your passwords: ")
    while len(password) <= MINIMUM_PASSWORD :
        print("invalid password")
        password = input("Please enter your passwords: ")
    return password

def asterisks(password):
    print(len(password) * "*")


main()