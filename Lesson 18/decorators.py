def log_transactions(func):
    """Декоратор для логирования"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Лог: {func.__name__} вызвана с аргументами {args[1:]} и результатом {result}")
        return result

    return wrapper