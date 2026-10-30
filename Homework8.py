# Список задач
tasks = ["Сделать домашнюю работу", "Помыть посуду", "Прочитать книгу"]
task_iterator = iter(tasks)

current_task = ''
print("Доступные команды: next, list, exit")
while True:
    command = input("\nВведите команду: ").strip().lower()

    if command == "next":
        try:
            #Вывод текущей задачи
            current_task = next(task_iterator)
            print(f"Текущая задача: {current_task}")
        except StopIteration:
            print("Все задачи выполнены")
            break

    elif command == "list":
        # Выводим оставшиеся задачи
        if current_task == '':
            remaining = tasks
        else:
            idx = tasks.index(current_task)
            remaining = tasks[idx + 1:]

        if remaining:
            print("Оставшиеся задачи:")
            for task in remaining:
                print(f"- {task}")
        else:
            print("Нет оставшихся задач.")

    elif command == "exit":
        # Выход из программы
        print("Выход из программы. До свидания!")
        break

    else:
        #Проверка команды
        print(f"Ошибка: команда '{command}' не поддерживается (используйте next, list, exit).")
