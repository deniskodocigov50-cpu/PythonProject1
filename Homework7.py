import user_manager
users_database = {}
print("Программа управления пользователями запущена.")
print("Доступные команды: add, remove, list, exit")
while True:
    # Запрашиваем команду у пользователя
    command = input("\nВведите команду: ").strip().lower()

    if command == "add":
        name = input("Введите имя пользователя: ").strip()
        if not name:
            print("Ошибка: Имя не может быть пустым.")
            continue
        age = input("Введите возраст пользователя: ").strip()
        user_manager.add_user(users_database, name, age)

    elif command == "remove":
        name = input("Введите имя пользователя для удаления: ").strip()
        user_manager.remove_user(users_database, name)

    elif command == "list":
        user_manager.list_users(users_database)

    elif command == "exit":
        print("Завершение работы программы. До свидания!")
        break

    else:
        print("Ошибка: Неизвестная команда. Попробуйте снова (add, remove, list, exit).")
