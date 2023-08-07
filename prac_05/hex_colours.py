NAME_TO_CODE = {"Aqua": "#00ffff", "Baby Blue": "#89cff0",
                "Baby Pink": "#f4c2c2", "Banana Mania": "#fae7b5",
                "Battleship Gray": "#848482", "Bitter Lemon": "#cae00d",
                "Chocolate1": "#ff7f24", "Corn": "#fbec5d",
                "Dark Brown": "#654321", "Dark Green": "#006400", }
print(NAME_TO_CODE)

colour_name = input("Enter the name of colour: ").title()
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(colour_name, "is", NAME_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter the name of colour: ").title()

for name, code in NAME_TO_CODE.items():
    print(f"{name:3s} is {code}")