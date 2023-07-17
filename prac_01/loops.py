for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

numbers = int(input("Number of stars: "))
for i in range(numbers) :
    print("*", end=' ')
print()

numbers = int(input("Number of stars: "))
for i in range(numbers) :
    for z in range(0,i+1):
        print("*", end="")
    print()

