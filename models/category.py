class Category:
    def __init__(self, name):
        self.name = name

class Income(Category):
    def __init__(self):
        super().__init__("Income")

class Expense(Category):
    def __init__(self):
        super().__init__("Expense")
