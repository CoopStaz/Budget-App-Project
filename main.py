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
        # Check if the budget has enough funds
        if self.check_funds(amount):
            # Deduct amount from balance and appends amount and description to the ledger list
            self.balance -= amount
            self.ledger.append({
                'amount': -abs(amount),
                'description': description,
            })
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        # Check if the budget has enough funds
        if self.check_funds(amount):
            # Add transaction to ledger list
            self.ledger.append({
                'amount': -abs(amount),
                'description': f"Transfer to {category}",
            })
            self.balance -= amount

            # Transfer amount to other category with description
            category.deposit(amount, f"Transfer from {self.name}")
            return True

    def check_funds(self, amount):
        # Return false if category balance is less than amount
        if self.balance < amount:
            return False
        return True


def create_spend_chart(categories):
    pass
