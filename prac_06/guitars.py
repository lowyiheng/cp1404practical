from guitar import Guitar
global year,cost
guitars = []
print("My guitars!")
while True:
    name: str = input("Name: ")
    if name == "":
        break
    year = input("Year: ")
    cost = input("$")
    temp = Guitar(name,year,cost)
    print(str(temp) + "added.")
    guitars.append(temp)
print("...snip...")
print("These are my guitars:")
count = 1
for guitar in guitars:
    if guitar.is_vintage():
        print(f"Guitars{count} {name}({year}),worth ${cost}(vintage)")
    else:
        print(f"Guitars{count} {name}({year}),worth ${cost}")