class Employee:
    def __init__(self, fn, ln, s):
        self.first_name = fn
        self.last_name = ln
        self.salary = s
    def get_info(self):
        return f'{self.first_name} {self.last_name}'
    def get_salary(self):
        return self.salary
