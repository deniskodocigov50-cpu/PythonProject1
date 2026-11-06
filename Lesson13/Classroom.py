class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_grade_to_student(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                return f'Оценка {grade} добавлена для {name}'
        return f'Студент не найден'

    def show_students(self):
        if not self.students:
            print('Студенты отсутствуют')
        else:
            print('Список студентов: ')
            for student in self.students:
                print(f'{student.name} - средний балл: {student.average_grade()}')
