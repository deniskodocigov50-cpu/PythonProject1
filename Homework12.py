# Стек для задач
task_stack = []
# Очередь на помощь
help_queue = []

print('Программа управления процессом учёбы')

while True:
    # Запрос основного режима работы
    print("\nВыберите режим работы:")
    print("1 — Управлять списком задач (Стек)")
    print("2 — Организовать очередь на помощь (Очередь)")
    print("Введите 'exit' для завершения работы.")

    main_choice = input("Ваш выбор: ").strip().lower()

    if main_choice == 'exit':
        print("Программа завершена.")
        break

    #Стек для задач
    elif main_choice == '1':
        while True:
            print("\n[Управление задачами (Стек)]")
            print("1 — Добавить задачу")
            print("2 — Удалить задачу")
            print("3 — Просмотреть текущий список задач")
            print("Введите 'back' для возврата в главное меню.")

            action = input("Выберите действие: ").strip().lower()

            if action == 'back':
                break
            elif action == '1':
                task = input("Введите название задачи: ").strip()
                if task:
                    task_stack.append(task)
                    print(f"Задача '{task}' успешно добавлена в стек.")
                else:
                    print("Название задачи не может быть пустым.")
            elif action == '2':
                if task_stack:
                    # Удаляем последний добавленный элемент
                    completed_task = task_stack.pop()
                    print(f"Задача '{completed_task}' отмечена как завершённая и удалена.")
                else:
                    print("Список задач пуст. Нечего удалять.")
            elif action == '3':
                if task_stack:
                    print("Текущий список задач (сверху вниз):")
                    # Отображаем в порядке от последней к первой
                    for i, task in enumerate(reversed(task_stack), 1):
                        print(f"{i}. {task}")
                else:
                    print("Список задач пуст.")
            else:
                print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 3 или 'back'.")

    # Очередь
    elif main_choice == '2':
        while True:
            print("\n[Очередь на помощь (Очередь)]")
            print("1 — Добавить человека в очередь")
            print("2 — Обслужить первого в очереди")
            print("3 — Просмотреть текущую очередь")
            print("Введите 'back' для возврата в главное меню.")

            action = input("Выберите действие: ").strip().lower()

            if action == 'back':
                break
            elif action == '1':
                person = input("Введите имя человека: ").strip()
                if person:
                    help_queue.append(person)
                    print(f"{person} добавлен(а) в очередь на помощь.")
                else:
                    print("Имя не может быть пустым.")
            elif action == '2':
                if help_queue:
                    # Удаляем первого пришедшего
                    served_person = help_queue.pop(0)
                    print(f"Помощь оказана пользователю: {served_person}. Удален(а) из очереди.")
                else:
                    print("Очередь пуста. Помощь никому не требуется.")
            elif action == '3':
                if help_queue:
                    print("Текущая очередь на помощь (от первых к последним):")
                    for i, person in enumerate(help_queue, 1):
                        print(f"{i}. {person}")
                else:
                    print("Очередь пуста.")
            else:
                print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 3 или 'back'.")

    else:
        print("Критическая ошибка ввода. Используйте '1', '2' или 'exit'.")
