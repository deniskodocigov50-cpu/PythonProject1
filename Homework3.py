tasks = []

print("Доступные команды: add, remove, list, exit")

# Циклически запрашиваем команды у пользователя
while True:
    command = input("\nВведите команду: ").strip().lower()
    if command == 'exit':
        print("Программа завершена. До свидания!")
        break

    # Добавление новой задачи
    elif command == 'add':
        new_task = input("Введите описание задачи: ").strip()
        if new_task:
            tasks.append(new_task)
            print(f"Задача '{new_task}' успешно добавлена.")
        else:
            print("Ошибка: Описание задачи не может быть пустым.")

    # Вывод списка всех задач
    elif command == 'list':
        if not tasks:
            print("Список задач пуст.")
        else:
            print("Текущие задачи:")
            for index, task in enumerate(tasks):
                print(f"{index}: {task}")

    # Удаление задачи по индексу
    elif command == 'remove':
        if not tasks:
            print("Ошибка: Список задач пуст, удалять нечего.")
            continue

        index_input = input("Введите индекс задачи для удаления: ").strip()

        # Обработка ошибок ввода
        try:
            index = int(index_input)
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Задача '{removed_task}' успешно удалена.")
            else:
                print(f"Ошибка: Задачи с индексом {index} не существует.")
        except ValueError:
            print("Ошибка: Введите корректное целое число для индекса.")

    # Если введена неизвестная команда
    else:
        print("Неизвестная команда. Попробуйте еще раз (add, remove, list, exit).")
