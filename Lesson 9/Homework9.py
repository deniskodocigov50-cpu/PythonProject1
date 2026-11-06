def number_sequence(start: int, end: int, even: bool = True):
    #Генератор
    for num in range(start, end + 1):
        if even and num % 2 == 0:
            yield num
        elif not even and num % 2 != 0:
            yield num


print("Программа генерации последовательности чисел")

# Запрос начала диапазона
while True:
    try:
        start_input = input("Введите начало диапазона (целое число): ")
        start = int(start_input)
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

# Запрос конца диапазона
while True:
    try:
        end_input = input("Введите конец диапазона (целое число): ")
        end = int(end_input)
        if end < start:
             print(f"Предупреждение: Конец диапазона меньше начала. Будет сгенерирована пустая последовательность.")
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")

# Запрос типа чисел
while True:
    choice = input("Какую последовательность вывести? (четные / нечетные): ").strip().lower()
    if choice in ['четные', 'чётные', 'even']:
        even_flag = True
        break
    elif choice in ['нечетные', 'нечётные', 'odd']:
        even_flag = False
        break
    else:
        print("Ошибка: введите 'четные' или 'нечетные'.")

# Вызов генератора и вывод результата
print("\nРезультат генерации:")
sequence = number_sequence(start, end, even=even_flag)

# Превращаем генератор в список
result_list = list(sequence)

if result_list:
    print(", ".join(map(str, result_list)))
else:
    print("В указанном диапазоне нет подходящих чисел.")
