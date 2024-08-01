class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        # Appends the amount and description to the ledger list
        self.ledger.append({
            'amount': amount,
            'description': description,
        })

        # Adds to the total balance
        self.balance += amount

    def withdraw(self, amount, description=""):
        # Return false if insufficient funds
        if self.balance < amount:
            return False

        # If sufficient funds deduct amount from balance and append info to the ledger list
        self.balance -= amount
        negative_amount = -abs(amount)
        self.ledger.append({
            'amount': negative_amount,
            'description': description,
        })
        return True

    def get_balance(self):
        pass

    def transfer(self):
        pass

    def check_funds(self):
        pass


def create_spend_chart(categories):
    pass
