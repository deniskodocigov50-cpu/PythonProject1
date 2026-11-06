def selection_sort(arr):
    # selection sort
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Ввод списка чисел
while True:
    try:
        user_input = input("Введите список чисел через пробел: ")
        # Преобразуем введенную строку в список целых чисел
        numbers = [int(x) for x in user_input.split()]

        if not numbers:
            print("Список не должен быть пустым.")
            continue
        break
    except ValueError:
        print("Ошибка: пожалуйста, вводите только целые числа через пробел.")

# Нахождение максимального значения
max_value = max(numbers)
print(f"Максимальное значение в списке: {max_value}")

# Сортировка списка выбором
sorted_numbers = selection_sort(numbers.copy())
print(f"Отсортированный список: {sorted_numbers}")

# Поиск количества вхождений числа
while True:
    try:
        search_input = input("Введите число для поиска: ")
        search_target = int(search_input)
        break
    except ValueError:
        print("Ошибка: нужно ввести одно целое число.")

# Подсчет вхождений
count = 0
for num in numbers:
    if num == search_target:
        count += 1

print(f"Число {search_target} встречается {count} раз(а) в списке.")
