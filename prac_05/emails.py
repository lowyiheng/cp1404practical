emails = input("Enter emails: ")
while emails != "":
    string = emails.split("@")[0].replace(".", " ")
    check = input(f"Is your name {string.title()} ? y/n>>> ")

    if check == "y":
        in_file = open("emails.txt", "a")
        in_file.write(f"{string.title()} ({emails})\n")
        in_file.close()

    elif check == "n":
        string = ''.join(filter(str.isalpha, emails.split('@')[0]))
        in_file = open("emails.txt", "a")
        in_file.write(f"{string.title()} ({emails})\n")
        in_file.close()
        print(f"Name: {string.title()}")

    else:
        print("Invalid enter")

    emails = input("Enter emails: ")

with open("emails.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    name_email = line.strip()
    print(name_email)