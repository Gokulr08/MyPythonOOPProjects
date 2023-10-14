class Student:
    def __init__(self, name, rollno, student_class):
        self.name = name
        self.rollno = rollno
        self.student_class = student_class

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f'Name: {student.name}, Rollno: {student.rollno}')
            print(f'Class: {student.student_class}')

if __name__ == '__main__':
    stud = StudentDatabase()

    while True:
        print('1. Add student')
        print('2. Display students')
        print('3. Quit')
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter your name: ")
            rollno = int(input("Enter your rollno: "))
            student_class = input("Enter your class: ")
            student = Student(name, rollno, student_class)
            stud.add_student(student)

        elif choice == '2':
            stud.display_students()

        elif choice == '3':
            print("Goodbye")
            break
