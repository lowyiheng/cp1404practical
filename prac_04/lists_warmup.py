numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])          # Output: 3
print(numbers[-1])         # Output: 2
print(numbers[3])          # Output: 1
print(numbers[:-1])        # Output: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])        # Output: [1]
print(5 in numbers)        # Output: True
print(7 in numbers)        # Output: False
print("3" in numbers)      # Output: False
print(numbers + [6, 5, 3]) # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Print all the elements from numbers except the first two (slice)
print(numbers[2:])         # Output: [4, 1, 5, 9, 1]
# Print whether 9 is an element of numbers
print(9 in numbers)        # Output: True