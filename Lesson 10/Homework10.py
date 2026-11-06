import os

filename = "notes.txt"

while True:
    # Запрос команды
    command = input("Введите команду (create, add, view, exit): ").strip().lower()

    if command == "create":
        # Создание нового файла или очистка существующего
        with open(filename, "w", encoding="utf-8") as f:
            pass  # Просто открываем файл, чтобы очистить его содержимое
        print(f"Файл '{filename}' создан и очищен.")

    elif command == "add":
        # Запрос текста заметки и запись в файл
        note = input("Заметка: ").strip()
        with open(filename, "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("Заметка добавлена.")

    elif command == "view":
        # Проверка
        if not os.path.exists(filename):
            print("Файл не найден. Сначала создайте файл.")
            continue

        # Чтение заметок из файла
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Проверка на пустоту файла
        if not lines:
            print("Файл пуст.")
        else:
            # Вывод заметок
            for index, line in enumerate(lines, start=1):
                print(f"{index}. {line.strip()}")

    elif command == "exit":
        # Завершение работы
        print("Программа завершена.")
        break

    else:
        # Обработка неверного ввода
        print("Неизвестная команда. Попробуйте снова.")
