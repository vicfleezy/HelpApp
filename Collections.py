def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

name = input("Enter student name:\n")

grade1 = float(input("Enter grade 1:\n"))
grade2 = float(input("Enter grade 2:\n"))
grade3 = float(input("Enter grade 3:\n"))
grade4 = float(input("Enter grade 4:\n"))
grade5 = float(input("Enter grade 5:\n"))

grades_list = [grade1, grade2, grade3, grade4, grade5]

average_score = sum(grades_list) / len(grades_list)

final_grade = get_letter_grade(average_score)

print()
print(name)
print(f"Average: {average_score:.1f}")
print(f"Letter Grade: {final_grade}")