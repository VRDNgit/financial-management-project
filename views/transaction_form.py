import tkinter as tk
from tkinter import ttk

class TransactionForm(ttk.LabelFrame):
    def __init__(self, parent, on_save, on_clear):
        super().__init__(parent, text="Transaction details", padding=10)
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.amount = tk.StringVar()
        self.category = tk.StringVar(value="Expense")
        self.description = tk.StringVar()

        self._field("First name", self.first_name, 0)
        self._field("Last name", self.last_name, 1)
        self._field("Amount", self.amount, 2)
        ttk.Label(self, text="Type").grid(row=3, column=0, sticky="w", pady=4)
        ttk.Combobox(self, textvariable=self.category, values=("Income", "Expense"),
                     state="readonly", width=22).grid(row=3, column=1, sticky="ew", pady=4)
        self._field("Description", self.description, 4)

        buttons = ttk.Frame(self)
        buttons.grid(row=5, column=0, columnspan=2, sticky="w", pady=10)
        ttk.Button(buttons, text="Save", command=on_save).pack(side="left", padx=(0, 5))
        ttk.Button(buttons, text="Clear", command=on_clear).pack(side="left")
        self.columnconfigure(1, weight=1)

    def _field(self, label, variable, row):
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=4)
        ttk.Entry(self, textvariable=variable).grid(row=row, column=1, sticky="ew", pady=4)

    def get_values(self):
        return {"first_name": self.first_name.get(), "last_name": self.last_name.get(),
                "amount": self.amount.get(), "category": self.category.get(),
                "description": self.description.get()}

    def fill(self, payment):
        self.first_name.set(payment.person.first_name)
        self.last_name.set(payment.person.last_name)
        self.amount.set(str(payment.amount))
        self.category.set(payment.category.name)
        self.description.set(payment.description)

    def clear(self):
        self.first_name.set("")
        self.last_name.set("")
        self.amount.set("")
        self.category.set("Expense")
        self.description.set("")
