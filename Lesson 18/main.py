from FinanceManager import FinanceManager
if __name__ == "__main__":
    manager = FinanceManager()
    manager.load_data()
    manager.run()