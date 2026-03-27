def getStudent(directory, student):
    if student in directory:
        return directory[student]
    else:
        print("Student not found")


def getStudentGrades(directory, student):
    if student in directory:
        return directory[student]["grades"]
    else:
        print("Student not found")


def getStudentGradeLevel(directory, student):
    if student in directory:
        return directory[student]["gradeLevel"]
    else:
        print("Student not found")


def getStudentEmail(directory, student):
    if student in directory:
        return directory[student]["Email"]
    else:
        print("Student not found")


def getStudentsByGradeLevel(directory, gradelevel):
    for student in directory:
        if directory[student]["gradeLevel"] == gradelevel:
            print(student)


def addStudent(directory):
    name = input("What is the student's name? ")
    email = input("What is the student's email? ")
    gradeLevel = int(input("What is the student's grade level? "))

    grades = {}
    grades["English"] = int(input("Enter English grade: "))
    grades["Math"] = int(input("Enter Math grade: "))
    grades["History"] = int(input("Enter History grade: "))
    grades["Religion"] = int(input("Enter Religion grade: "))

    directory[name] = {
        "Email": email,
        "gradeLevel": gradeLevel,
        "grades": grades
    }

    print("Student added")


def removeStudent(directory, student):
    if student in directory:
        del directory[student]
        print("Student removed")
    else:
        print("Student not found")


def changeGrades(directory, student):
    if student in directory:
        print("Enter new grades:")
        directory[student]["grades"]["English"] = int(input("English: "))
        directory[student]["grades"]["Math"] = int(input("Math: "))
        directory[student]["grades"]["History"] = int(input("History: "))
        directory[student]["grades"]["Religion"] = int(input("Religion: "))
        print("Grades updated")
    else:
        print("Student not found")


def calculateGPA(directory, student):
    if student in directory:
        grades = directory[student]["grades"]
        total = sum(grades.values())
        GPA = total / len(grades)
        return GPA
    else:
        print("Student not found")
        return 0


def checkHonorRoll(directory, student):
    if student in directory:
        grades = directory[student]["grades"]
        GPA = calculateGPA(directory, student)

        all_above_81 = all(grade > 81 for grade in grades.values())

        if GPA >= 88 and all_above_81:
            return True
        else:
            return False
    else:
        print("Student not found")
        return False


def printMenu():
    print("\n--- Student Directory ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Get Student Info")
    print("4. Change Grades")
    print("5. Calculate GPA")
    print("6. Check Honor Roll")
    print("7. Get Students by Grade Level")
    print("8. Exit")


def main():
    Students = {
        "John Smith": {
            "Email": "john@gmail.com",
            "gradeLevel": 4,
            "grades": {"English": 83, "Math": 74, "History": 92, "Religion": 97}
        },
        "Michael Scott": {
            "Email": "michael@gmail.com",
            "gradeLevel": 3,
            "grades": {"English": 94, "Math": 82, "History": 77, "Religion": 90}
        }
    }

    running = True

    while running:
        printMenu()
        choice = int(input("Choose an option: "))

        if choice == 1:
            addStudent(Students)

        elif choice == 2:
            name = input("Enter student name: ")
            removeStudent(Students, name)

        elif choice == 3:
            name = input("Enter student name: ")
            print(getStudent(Students, name))

        elif choice == 4:
            name = input("Enter student name: ")
            changeGrades(Students, name)

        elif choice == 5:
            name = input("Enter student name: ")
            print("GPA:", calculateGPA(Students, name))

        elif choice == 6:
            name = input("Enter student name: ")
            print("Honor Roll:", checkHonorRoll(Students, name))

        elif choice == 7:
            level = int(input("Enter grade level: "))
            getStudentsByGradeLevel(Students, level)

        elif choice == 8:
            running = False

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
