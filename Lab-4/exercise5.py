
# Lab 4 - Problem 5: Fibonacci Numbers Below N

n = int(input("Enter the limit N: "))

a = 0
b = 1

while a < n:
    print(a)
    a, b = b, a + b
