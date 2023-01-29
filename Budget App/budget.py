class category():
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.__balance = 0.0
    
    def __repr__(self) -> str:
        title = self.name.center(30, '*') + '\n'
        ledger = ""

        for item in self.ledger:
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.__balance)

        return title + ledger + total

    def get_balance(self):
        return self.__balance

    def deposit(self, amount, description=''):
        self.__balance += amount
        return self.ledger.append({'amount': amount, 'description':description})

    def withdrawal(self,amount, description=''):
        if self.check_funds(amount):
            self.__balance -= amount
            self.ledger.append({'amount': -amount, 'description':description})
            return True
        else:
            return False

    def check_funds(self, amount):
        return False if self.get_balance() < amount else True

    def transfer(self, amount, destination, name):
        if self.check_funds(amount):
            self.withdrawal(amount, f'Transfer to {name}')
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
   
def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))
    
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    
    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")

