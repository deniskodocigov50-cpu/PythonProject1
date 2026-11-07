from Employee import Employee

class Intern(Employee):
    def __init__(self, fn, ln, s, dr):
        super().__init__(fn, ln, s)
        self.discount_rate = dr

    def get_salary(self):
        return super().get_salary() * self.discount_rate
