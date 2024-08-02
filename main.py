class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:>7.2f}"
            items += f"{description:<23}{amount}\n"
        total = f"Total: {self.balance:.2f}"
        return title + items + total

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
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        # Check if the budget has enough funds
        if self.check_funds(amount):
            # Add transaction to ledger list
            self.ledger.append({
                'amount': -abs(amount),
                'description': f"Transfer to {category.name}",
            })
            self.balance -= amount

            # Transfer amount to other category with description
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Return false if category balance is less than amount
        if self.balance < amount:
            return False
        return True

    def get_withdrawals(self):
        return sum(entry['amount'] for entry in self.ledger if entry['amount'] < 0)


def create_spend_chart(categories):
    # Calculate total withdrawals and percentage spent per category
    total_withdrawals = sum(category.get_withdrawals() for category in categories)
    percentages = [(category.get_withdrawals() / total_withdrawals) * 100 for category in categories]

    # Create the chart title
    chart = "Percentage spent by category\n"

    # Add the bars to the chart
    for i in range(100, -10, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"

    # Add the category names vertically
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart


# Example usage
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(15, 'gas')
auto.withdraw(30, 'repair')

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))