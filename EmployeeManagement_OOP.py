class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(f"ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}, Salary: {employee.salary}")

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        return None

if __name__ == '__main__':
    employee_db = EmployeeDatabase()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee's name: ")
            position = input("Enter employee's position: ")
            salary = input("Enter employee's salary: ")
            employee = Employee(emp_id, name, position, salary)
            employee_db.add_employee(employee)
        elif choice == '2':
            print("\nList of Employees:")
            employee_db.display_employees()
        elif choice == '3':
            emp_id = input("Enter employee ID to search: ")
            employee = employee_db.search_employee(emp_id)
            if employee:
                print(f"Employee Found - ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}, Salary: {employee.salary}")
            else:
                print("Employee not found.")
        elif choice == '4':
            print("Goodbye!")
            break
