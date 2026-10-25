
# Lab 4 - Problem 4: Sum of All Prime Numbers Below 1000

total = 0

for number in range(2, 1000):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        total += number

print("Sum of all prime numbers below 1000:", total)
