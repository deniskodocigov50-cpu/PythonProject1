# Запрашиваем ввод участников в строгом соответствии с примером
set1 = set(input("Введите участников первого конкурса через пробел: ").split())
set2 = set(input("Введите участников второго конкурса через пробел: ").split())
set3 = set(input("Введите участников третьего конкурса через пробел: ").split())

#Участники всех трех конкурсов
all_three = set1 & set2 & set3

#Участники хотя бы одного конкурса
at_least_one = set1 | set2 | set3

#Участники только одного конкурса
only_one = (set1 - (set2 | set3)) | (set2 - (set1 | set3)) | (set3 - (set1 | set2))

#Участники ровно двух конкурсов
exactly_two = ((set1 & set2) | (set2 & set3) | (set1 & set3)) - all_three

#Вывод результатов
print(f"Участники всех трёх конкурсов: {all_three if all_three else 'set()'}")
print(f"Участники хотя бы одного конкурса: {at_least_one if at_least_one else 'set()'}")
print(f"Участники только одного конкурса: {only_one if only_one else 'set()'}")
print(f"Участники ровно двух конкурсов: {exactly_two if exactly_two else 'set()'}")