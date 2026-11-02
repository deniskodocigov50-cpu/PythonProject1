#словарь для участников
participants_registry = {}

print("Программа управления реестром участников мероприятия")
print("Доступные команды: add, remove, list, exit")

# Основной цикл программы
while True:
    # Запрос команды
    command = input("\nВведите команду (add, remove, list, exit): ").strip().lower()

    if command == 'add':
        print("\nРегистрация нового участника")
        first_name = input("Введите имя: ").strip()
        last_name = input("Введите фамилию: ").strip()

        # Проверка на корректность
        if not first_name or not last_name:
            print("Ошибка: Имя и фамилия не могут быть пустыми!")
            continue

        # Создание ключа
        participant_key = (first_name, last_name)

        # Запрос интересов
        interests_input = input("Введите интересы (через запятую): ")

        # Создание множества интересов
        interests_set = {interest.strip() for interest in interests_input.split(',') if interest.strip()}

        # Добавление в словарь
        if participant_key in participants_registry:
            # объединяем интересы
            participants_registry[participant_key].update(interests_set)
            print(f"Информация об участнике {first_name} {last_name} обновлена.")
        else:
            participants_registry[participant_key] = interests_set
            print(f"Участник {first_name} {last_name} успешно зарегистрирован.")

    elif command == 'remove':
        print("\nУдаление участника из реестра")
        first_name = input("Введите имя участника для удаления: ").strip()
        last_name = input("Введите фамилию участника для удаления: ").strip()

        participant_key = (first_name, last_name)

        # Обработка ошибок
        if participant_key in participants_registry:
            del participants_registry[participant_key]
            print(f"Участник {first_name} {last_name} успешно удален из реестра.")
        else:
            print(f"Ошибка удаления: Участник {first_name} {last_name} не найден в реестре.")

    elif command == 'list':
        print("\nПолный список участников")
        # Проверка, не пуст ли реестр
        if not participants_registry:
            print("Реестр участников пуст.")
        else:
            # Итерация по словарю
            for (first_name, last_name), interests in participants_registry.items():
                interests_str = ", ".join(interests) if interests else "нет интересов"
                print(f" {first_name} {last_name}  интересы: {interests_str}")

    elif command == 'exit':
        print("\nПрограмма завершена. Всего доброго!")
        break

    else:
        # Обработка ввода неизвестной команды
        print("Ошибка: Неизвестная команда. Пожалуйста, используйте add, remove, list или exit.")