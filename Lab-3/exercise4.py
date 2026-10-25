
# Lab 3 - Problem 4: Vowel Checker

character = input("Enter a character: ")

if len(character) == 1 and character.lower() in "aeiou":
    print(character, "is a vowel")
else:
    print(character, "is not a vowel")
