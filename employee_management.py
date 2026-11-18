class Employee:
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role

    def display(self):
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print("--------------------")


employees = [
    Employee(101, "Vasavi", "DevOps Engineer"),
    Employee(102, "Srihari", "Cloud Engineer"),
    Employee(103, "Rahul", "Software Developer")
]

print("EMPLOYEE MANAGEMENT SYSTEM")
print("==========================")

for employee in employees:
    employee.display()
