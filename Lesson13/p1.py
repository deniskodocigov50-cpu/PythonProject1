from Lesson13.Classroom import Classroom
from Lesson13.Student import Student
classroom = Classroom()
while True:
    cmd = input('> Введите команду(add_student, add_grade, show, exit):  ')
    if cmd == 'add_student':
        name = input('Введите имя ученика: ')
        classroom.add_student(Student(name))
        print(f'Студент {name} добавлен')
    elif cmd == 'add_grade':
        name = input('Введите имя ученика: ').strip()
        grade = float(input('Введите оценку: '))
        print(classroom.add_grade_to_student(name, grade))
    elif cmd == 'show':
        classroom.show_students()
    elif cmd == 'exit':
        print('Программа завершена')
        break
    else:
        print('Неизвестная команда')

