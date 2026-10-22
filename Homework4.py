# 1. Запрашиваем данные у пользователя
first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
letter_text = input("Введите текст основного сообщения: ")

# 2. Обрабатываем регистр букв
first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()

# 3. Формируем и выводим готовое письмо
print(f"\nУважаемый {first_name} {last_name},")
print(letter_text)
print(f"С уважением, {first_name} {last_name}")
