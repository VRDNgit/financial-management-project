import json
from pathlib import Path

class Storage:
    def __init__(self):
        self.data_file = Path(__file__).resolve().parent.parent / "data" / "payments.json"
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            self.save([])

    def load(self):
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Saved data must be a list.")
            return data
        except FileNotFoundError:
            self.save([])
            return []
        except (json.JSONDecodeError, OSError, ValueError) as error:
            raise RuntimeError(f"Could not read saved data: {error}") from error

    def save(self, payments):
        try:
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump(payments, file, ensure_ascii=False, indent=4)
        except (OSError, TypeError, ValueError) as error:
            raise RuntimeError(f"Could not save data: {error}") from error
