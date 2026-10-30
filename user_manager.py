def add_user(users, name, age):
    """Добавляет пользователя в словарь users."""
    try:
        age_int = int(age)
        if age_int < 0 or age_int > 150:
            print("Ошибка: Введен некорректный возраст (должен быть от 0 до 150).")
            return
    except ValueError:
        print("Ошибка: Возраст должен быть числом.")
        return

    users[name] = age_int
    print(f"Пользователь {name} успешно добавлен.")


def remove_user(users, name):
    """Удаляет пользователя по имени."""
    if name in users:
        del users[name]
        print(f"Пользователь {name} успешно удален.")
    else:
        print(f"Ошибка: Пользователь с именем '{name}' не найден.")


def list_users(users):
    """Выводит список всех пользователей."""
    if not users:
        print("Список пользователей пуст.")
        return

    print("\nСписок пользователей:")
    for name, age in users.items():
        print(f"Имя: {name}, Возраст: {age}")