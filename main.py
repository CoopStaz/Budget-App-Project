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
        self.ledger.append({
            'amount': -abs(amount),
            'description': description,
        })
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        # Return false if insufficient funds
        if self.balance < amount:
            return False

        # Add transaction to ledger list
        self.ledger.append({
            'amount': -abs(amount),
            'description': f"Transfer to {category}",
        })
        self.balance -= amount

        # Transfer amount to other category with description
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self):
        pass


def create_spend_chart(categories):
    pass
