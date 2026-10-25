
# Lab 3 - Problem 5: Student Grade Calculator

marks = float(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Letter Grade: A+")
    print("Grade Point: 4.00")
elif marks >= 85:
    print("Letter Grade: A")
    print("Grade Point: 3.75")
elif marks >= 80:
    print("Letter Grade: B+")
    print("Grade Point: 3.50")
elif marks >= 75:
    print("Letter Grade: B")
    print("Grade Point: 3.25")
elif marks >= 70:
    print("Letter Grade: C+")
    print("Grade Point: 3.00")
elif marks >= 65:
    print("Letter Grade: C")
    print("Grade Point: 2.75")
elif marks >= 60:
    print("Letter Grade: D+")
    print("Grade Point: 2.50")
elif marks >= 50:
    print("Letter Grade: D")
    print("Grade Point: 2.25")
else:
    print("Letter Grade: F")
    print("Grade Point: 0.00")
