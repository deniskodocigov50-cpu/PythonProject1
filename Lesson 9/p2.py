def generator(s, e):
    for n in range(s, e+1):
        if n % 2 == 0:
            yield n

start = int(input('Введите начало диапозона: '))
end = int(input('Введите конец диапозона: '))

