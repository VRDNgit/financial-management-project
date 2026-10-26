<div align="center">

# 💰 Financial Management System

### A Simple Desktop Application for Managing Financial Transactions

Built with **Python** and **Tkinter** 🐍

Manage your financial transactions through a simple and user-friendly graphical interface.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-FFCA28?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Desktop-2ea44f?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In_Development-orange?style=for-the-badge)

</div>

---

## 📌 About The Project

**Financial Management System** is a Python desktop application designed to make managing financial transactions simple and convenient.

The application provides a graphical user interface built with Tkinter, allowing users to manage transaction records without interacting directly with the command line.

The project is structured into separate modules to keep the code organized, readable, and easier to maintain.

### ✨ Features

* ➕ **Add Transactions** — Register new financial transactions.
* 🗑️ **Delete Transactions** — Remove existing transaction records.
* 📋 **View Transactions** — Display transaction information in a structured table.
* 🖥️ **Graphical User Interface** — Interact with the application through a Tkinter-based interface.
* 🧩 **Modular Architecture** — Separate components for models, services, utilities, and views.

---

## 🛠️ Built With

| Technology       | Purpose                                                   |
| ---------------- | --------------------------------------------------------- |
| 🐍 Python        | Core application logic                                    |
| 🖥️ Tkinter      | Graphical user interface                                  |
| 📊 Tkinter `ttk` | Table-based data presentation, if used by the application |
| 📦 Git & GitHub  | Version control and project hosting                       |

---

## 📂 Project Structure

```text
financial-management-project/
│
├── main.py
│
├── models/
│   ├── category.py
│   ├── payments.py
│   └── person.py
│
├── services/
│   └── storage.py
│
├── utils/
│   └── validators.py
│
└── views/
    ├── main_window.py
    ├── transaction_form.py
    └── transaction_list.py
```

### 📁 Directory Overview

* **`main.py`** — Application entry point.
* **`models/`** — Modules representing application data and related models.
* **`services/`** — Service-layer functionality, including storage-related operations.
* **`utils/`** — Utility functions and validation logic.
* **`views/`** — Graphical interface components, including the main window, transaction form, and transaction list.

---

## ⚙️ Getting Started

Follow these steps to run the project locally.

### Prerequisites

Make sure you have:

* Python 3 installed.
* Git installed (if you want to clone the repository).

Tkinter is commonly included with standard Python installations. On some systems, it may need to be installed separately.

### 1. Clone the Repository

```bash
git clone https://github.com/VRDNgit/financial-management-project.git
```

### 2. Navigate to the Project Directory

```bash
cd financial-management-project
```

### 3. Run the Application

```bash
python main.py
```

If your system uses the Python launcher on Windows, you can also try:

```cmd
py main.py
```

---

## 🚀 Usage

Once the application starts:

1. Launch the desktop application.
2. Add a new financial transaction through the transaction form.
3. View registered transactions in the table.
4. Select a transaction and delete it when necessary.

The exact available fields and controls depend on the application's implementation.

---

## 🗺️ Future Improvements

Potential enhancements for future versions include:

* 🔍 Search and filter transactions.
* 🏷️ More advanced transaction categorization.
* 📅 Date-based transaction filtering.
* 📈 Financial summaries and statistics.
* 💾 Improved data persistence.
* 📤 Export transaction records to CSV or Excel.
* 🎨 Further improvements to the graphical interface.

*These are potential future enhancements, not necessarily features available in the current version.*

---

## 🎯 Project Goals

This project aims to provide a practical example of building a desktop application with Python while applying concepts such as:

* Object-Oriented Programming (OOP).
* Modular code organization.
* GUI development with Tkinter.
* Data validation.
* Separation of application logic and presentation.

---

## 👨‍💻 Author

**VRDNgit**

GitHub: [@VRDNgit](https://github.com/VRDNgit)

---

<div align="center">

### 💻 Built with Python. Designed for Simplicity.

⭐ If you find this project useful, consider giving it a star!

</div>
