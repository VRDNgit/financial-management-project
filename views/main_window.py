import tkinter as tk
from tkinter import ttk, messagebox
from models.person import Person
from models.category import Income, Expense
from models.payments import Payment
from services.storage import Storage
from utils.validators import validate_person, validate_amount
from views.transaction_form import TransactionForm
from views.transaction_list import TransactionList

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Personal Finance Manager")
        self.root.geometry("850x500")
        self.root.minsize(700, 420)
        self.storage = Storage()
        self.payments = []
        self.selected_id = None
        self.income_text = tk.StringVar(value="Income: 0.00")
        self.expense_text = tk.StringVar(value="Expense: 0.00")
        self.balance_text = tk.StringVar(value="Balance: 0.00")
        self._build_window()
        self._load_payments()

    def _build_window(self):
        main = ttk.Frame(self.root, padding=12)
        main.pack(fill="both", expand=True)
        ttk.Label(main, text="Personal Finance Manager",
                  font=("Arial", 16, "bold")).pack(anchor="w", pady=(0, 10))
        summary = ttk.Frame(main)
        summary.pack(fill="x", pady=(0, 10))
        for text in (self.income_text, self.expense_text, self.balance_text):
            ttk.Label(summary, textvariable=text).pack(side="left", padx=(0, 18))
        content = ttk.Frame(main)
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=2)
        content.rowconfigure(0, weight=1)
        self.form = TransactionForm(content, self.save_payment, self.clear_form)
        self.form.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.transaction_list = TransactionList(content, self.select_payment)
        self.transaction_list.grid(row=0, column=1, sticky="nsew")
        ttk.Button(main, text="Delete selected", command=self.delete_payment).pack(
            anchor="e", pady=(8, 0))

    def _load_payments(self):
        try:
            self.payments = [Payment.from_dict(row) for row in self.storage.load()]
            next_id = 1
            for p in self.payments:
                try:
                    p.payment_id = int(p.payment_id)
                    next_id = max(next_id, p.payment_id + 1)
                except (ValueError, TypeError):
                    p.payment_id = next_id
                    next_id += 1
            self._refresh()
        except (RuntimeError, ValueError, TypeError, KeyError) as error:
            messagebox.showerror("Loading error", str(error), parent=self.root)
            self.payments = []
            self._refresh()

    def save_payment(self):
        values = self.form.get_values()
        valid, message = validate_person(values["first_name"], values["last_name"])
        if not valid:
            messagebox.showwarning("Check input", message, parent=self.root)
            return
        valid, amount, message = validate_amount(values["amount"])
        if not valid:
            messagebox.showwarning("Check input", message, parent=self.root)
            return
        try:
            person = Person(values["first_name"], values["last_name"])
            category = Income() if values["category"] == "Income" else Expense()
            if self.selected_id is None:
                new_id = max((p.payment_id or 0 for p in self.payments), default=0) + 1
                self.payments.append(Payment(person, amount, category,
                    values["description"], payment_id=new_id))
            else:
                payment = self._find_payment(self.selected_id)
                if payment is None:
                    messagebox.showwarning("Not found", "Select the transaction again.", parent=self.root)
                    self.clear_form()
                    return
                payment.person, payment.amount, payment.category = person, amount, category
                payment.description = values["description"].strip()
            self._save_to_file()
            self._refresh()
            self.clear_form()
        except (RuntimeError, OSError, ValueError, TypeError) as error:
            messagebox.showerror("Save error", str(error), parent=self.root)

    def select_payment(self, item_id):
        try:
            payment = self._find_payment(int(item_id))
            if payment:
                self.selected_id = payment.payment_id
                self.form.fill(payment)
        except (ValueError, TypeError):
            messagebox.showwarning("Selection error", "Could not select this transaction.", parent=self.root)

    def delete_payment(self):
        if self.selected_id is None:
            messagebox.showinfo("Select transaction", "Click a transaction first.", parent=self.root)
            return
        if not messagebox.askyesno("Confirm", "Delete this transaction?", parent=self.root):
            return
        try:
            payment = self._find_payment(self.selected_id)
            if payment:
                self.payments.remove(payment)
                self._save_to_file()
                self._refresh()
            self.clear_form()
        except (RuntimeError, ValueError, TypeError) as error:
            messagebox.showerror("Delete error", str(error), parent=self.root)

    def clear_form(self):
        self.form.clear()
        self.selected_id = None
        for item in self.transaction_list.tree.selection():
            self.transaction_list.tree.selection_remove(item)

    def _find_payment(self, payment_id):
        return next((p for p in self.payments if p.payment_id == payment_id), None)

    def _save_to_file(self):
        self.storage.save([p.to_dict() for p in self.payments])

    def _refresh(self):
        self.transaction_list.refresh(self.payments)
        income = sum(p.amount for p in self.payments if p.category.name == "Income")
        expense = sum(p.amount for p in self.payments if p.category.name == "Expense")
        self.income_text.set(f"Income: {income:,.2f}")
        self.expense_text.set(f"Expense: {expense:,.2f}")
        self.balance_text.set(f"Balance: {income - expense:,.2f}")

    def run(self):
        try:
            self.root.mainloop()
        except tk.TclError as error:
            messagebox.showerror("Application error", str(error))
        finally:
            try:
                self.root.destroy()
            except tk.TclError:
                pass
