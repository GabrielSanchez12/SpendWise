import json
from pathlib import Path

from .expenses import Expense


DATA_FILE = Path("data/expenses.json")


def load_expenses() -> list[Expense]:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [
        Expense(
            description=item["description"],
            amount=item["amount"],
            category=item["category"],
        )
        for item in data
    ]


def save_expenses(expenses: list[Expense]) -> None:
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            [expense.to_dict() for expense in expenses],
            file,
            indent=4,
        )