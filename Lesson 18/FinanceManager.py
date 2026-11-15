from decorators import log_transactions

class FinanceManager:
    def __init__(self, filename="transactions.txt"):
        """Инициализирует баланс и список транзакций."""
        self.filename = filename
        self.balance = 0.0
        self.transactions = []

    @log_transactions
    def add_transaction(self, type, amount, category):
        """Добавляет новую транзакцию (доход/расход), обновляет баланс и историю."""
        if type not in ("доход", "расход"):
            print("Ошибка: тип операции должен быть 'доход' или 'расход'.")
            return False
        if amount <= 0:
            print("Ошибка: сумма должна быть положительным числом.")
            return False
        if type == "расход" and amount > self.balance:
            print("Ошибка: недостаточно средств на балансе.")
            return False

        transaction = {
            "type": type,
            "amount": float(amount),
            "category": category
        }
        self.transactions.append(transaction)

        if type == "доход":
            self.balance += float(amount)
        else:
            self.balance -= float(amount)

        print(f"Транзакция добавлена: {transaction}")
        return True

    def get_transactions(self):
        """Возвращает список всех транзакций."""
        return self.transactions

    def get_balance(self):
        """Возвращает текущий баланс."""
        return self.balance

    def save_data(self):
        """Сохраняет данные в текстовый файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(f"balance:{float(self.balance)}\n")
            for t in self.transactions:
                file.write(f"{t['type']},{float(t['amount'])},{t['category']}\n")
        print("Данные успешно сохранены в файл.")

    def load_data(self):
        """ загружает данные из текстового файла. """
        try:
            with open("transactions.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                self._balance = float(lines[0].strip().split(":")[1])
                self._transactions = lines[1:]
                print("Данные успешно загружены из файла.")
        except FileNotFoundError:
            print("Файл данных не найден. Начинаем с пустого баланса.")
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")

        print("Данные успешно загружены из файла.")

    def run(self):
        """Отвечает за взаимодействие с пользователем и управляет циклом программы."""
        while True:
            print("\nМеню:")
            print("1. Добавить доход/расход")
            print("2. Показать баланс и транзакции")
            print("3. Сохранить и выйти")

            choice = input("Выберите действие: ").strip()

            if choice == "1":
                t_type = input("Введите тип (доход/расход): ").strip().lower()
                try:
                    amount = float(input("Введите сумму: ").strip())
                except ValueError:
                    print("Ошибка: сумма должна быть числом.")
                    continue

                category = input("Введите категорию: ").strip()
                if not category:
                    category = "без категории"

                self.add_transaction(t_type, amount, category)

            elif choice == "2":
                print(f"Текущий баланс: {self.get_balance()}")
                transactions = self.get_transactions()
                if not transactions:
                    print("Список транзакций пуст.")
                else:
                    print("Список транзакций:")
                    for t in transactions:
                        print(t)

            elif choice == "3":
                self.save_data()
                print("Программа завершена.")
                break

            else:
                print("Ошибка: неверный ввод команды. Выберите 1, 2 или 3.")