
# Lab 4 - Problem 3: Exponentiation

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

for i in range(exponent):
    result = result * base

print("Result:", result)
