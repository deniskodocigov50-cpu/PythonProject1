from Employee import Employee


class Manager(Employee):
    def __init__(self, fn, ln, s, b):
        super().__init__(fn, ln, s)
        self.bonus = b

    def get_salary(self):
        return super().get_salary() * self.bonus