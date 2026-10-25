from tkinter import ttk

class TransactionList(ttk.LabelFrame):
    def __init__(self, parent, on_select):
        super().__init__(parent, text="Saved transactions", padding=8)
        columns = ("person", "type", "amount", "date")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)
        labels = {"person": "Name", "type": "Type", "amount": "Amount", "date": "Date"}
        widths = {"person": 140, "type": 75, "amount": 100, "date": 140}
        for col in columns:
            self.tree.heading(col, text=labels[col])
            self.tree.column(col, width=widths[col], anchor="w")
        scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll.grid(row=0, column=1, sticky="ns")
        self.tree.bind("<<TreeviewSelect>>", lambda event: self._select(on_select))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def _select(self, callback):
        selected = self.tree.selection()
        if selected:
            callback(selected[0])

    def refresh(self, payments):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for p in payments:
            self.tree.insert("", "end", iid=str(p.payment_id),
                values=(p.person.full_name(), p.category.name, f"{p.amount:,.2f}", p.date))
