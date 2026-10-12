class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("cuenta creada")

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance and amount > 0:
            self.balance = self.balance - amount
            return self.balance

        raise ValueError("your accoutn has to little for this ")

    def get_balance(self):
        return self.balance
