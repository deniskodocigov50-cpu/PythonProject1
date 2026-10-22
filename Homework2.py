total_hours = 0

# 1. Цикл while для запроса количества учебных дней (от 1 до 7)
while True:
    try:
        days_input = input("Введите количество учебных дней за неделю (1-7): ")
        days = int(days_input)
        if 1 <= days <= 7:
            break
        else:
            print("Ошибка: количество дней должно быть от 1 до 7. Попробуйте снова.")
    except ValueError:
        print("Ошибка ввода: необходимо ввести целое число. Попробуйте снова.")

# 2. Цикл for для последовательного опроса каждого учебного дня
for day in range(1, days + 1):
    while True:
        # 3. Блоки try и except для обработки исключений при вводе часов
        try:
            hours_input = input(f"Введите количество часов учёбы для дня {day}: ")
            hours = float(hours_input)

            if hours >= 0:
                total_hours += hours
                break
            else:
                print("Ошибка: количество часов не может быть отрицательным.")
        except ValueError:
            print("Ошибка ввода: введите корректное числовое значение часов.")

# Вывод ожидаемого итогового результата
print(f"Общее количество часов учёбы за неделю: {total_hours}")
