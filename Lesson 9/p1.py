def generator(limit, divisor):
    for i in range(1, limit + 1):
        if i % divisor == 0:
            yield i

limit = int(input('Введите верхний предел: '))
divisor = int(input('Введите делитель: '))

print(f'Числа от 1 до {limit}, кратные {divisor}: ')
for i in generator(limit, divisor):
    print(i)

def generator2(l, d):
    return [n for n in range(1, l+1) if n % d == 0]

print(f'Числа от 1 до {limit}, кратные {divisor} (через генераторное выражение): ')
print(generator2(limit, divisor))