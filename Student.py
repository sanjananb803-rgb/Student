def calculate_grade(average):
    if 90 <= average <= 100:
        return "S"
    elif 80 <= average < 90:
        return "A"
    elif 65 <= average < 80:
        return "B"
    elif 50 <= average < 65:
        return "C"
    elif 40 <= average < 50:
        return "D"
    else:
        return "F"
def main():
    print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks in Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    average = sum(marks) / 3
    grade = calculate_grade(average)
    print("\n========== STUDENT DETAILS ==========")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    for i, mark in enumerate(marks, 1):
        print(f"Subject {i} Marks: {mark}")
    print("Total Marks:", sum(marks))
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("=====================================")
if __name__ == "__main__":
    main()
