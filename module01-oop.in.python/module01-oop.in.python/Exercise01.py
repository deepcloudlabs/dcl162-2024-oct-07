class InsufficientBalanceException(Exception):
    def __init__(self,message, deficit):
        super().__init__()
        self.message = message
        self.deficit = deficit

class Account:
    def __init__(self, iban, balance=5_000):
        # attributes/state/data: iban, balance
        self.iban = iban
        # constraint: self.balance must be always positive or zero
        self.balance = balance

    def deposit(self, amount):
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        self.balance = self.balance + amount
        return self.balance

    #business method
    def withdraw(self, amount):
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        # business rule
        if amount > self.balance:
            deficit = amount - self.balance
            # business exception
            raise InsufficientBalanceException("Your balance does not cover your expenses", deficit)
        self.balance = self.balance - amount
        return self.balance