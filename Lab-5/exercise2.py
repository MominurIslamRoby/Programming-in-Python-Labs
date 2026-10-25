# Lab 5 - Exercise 2: Student Marks Investigator
# Course: Programming in Python

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


def calculate_average(marks):
    """Return the average of marks; return None for missing or invalid marks."""
    if not marks:
        return None

    for mark in marks:
        if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
            return None

    return sum(marks) / len(marks)


def classify_performance(average):
    """Return the performance category specified in the lab manual."""
    if average is None:
        return "Invalid or missing marks"
    if average >= 80:
        return "Excellent"
    if average >= 70:
        return "Good"
    if average >= 60:
        return "Satisfactory"
    return "Needs Improvement"


def display_report(students):
    """Display each student's ID, name, average, and performance category."""
    if not students:
        print("No student records found.")
        return

    print("Student ID | Name | Average | Performance")
    for student in students:
        student_id, name, marks = student
        average = calculate_average(marks)

        if average is None:
            print(f"{student_id} | {name} | N/A | {classify_performance(average)}")
        else:
            print(
                f"{student_id} | {name} | {average:.2f} | "
                f"{classify_performance(average)}"
            )


if __name__ == "__main__":
    display_report(students)

    print("\nEDGE CASE TESTS")
    print("Equal marks [80, 80, 80]:", calculate_average([80, 80, 80]))
    print("Tied averages [70, 70]:", calculate_average([70, 70]))
    print("Invalid mark [70, 120]:", calculate_average([70, 120]))
    print("No marks []:", calculate_average([]))
