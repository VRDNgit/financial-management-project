from datetime import datetime
from models.person import Person
from models.category import Income, Expense

class Payment:
    def __init__(self, person, amount, category, description="", date=None, payment_id=None):
        self.person = person
        self.amount = float(amount)
        self.category = category
        self.description = description.strip()
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.payment_id = payment_id

    def to_dict(self):
        return {
            "id": self.payment_id,
            "first_name": self.person.first_name,
            "last_name": self.person.last_name,
            "amount": self.amount,
            "category": self.category.name,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        category = Income() if data.get("category") == "Income" else Expense()
        person = Person(data.get("first_name", ""), data.get("last_name", ""))
        return cls(person, data.get("amount", 0), category,
                   data.get("description", ""), data.get("date"), data.get("id"))
