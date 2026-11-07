from Employee import Employee
from Manager import Manager
from intern import Intern

employees = [
    Employee("Иван", "Иванов", 50000),
    Manager("Мария", "Петрова", 80000, 20000),
    Intern("Алексей", "Смирнов", 30000, 0.5)
]

for emp in employees:
    print(f"{emp.get_info()} - Зарплата: {emp.get_salary()}")