from dataclasses import dataclass

@dataclass
class Expense:
    description: str
    amount: float
    category: str

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
        }


def create_expense(description: str, amount: float, category: str) -> Expense:
    if not description.strip():
        raise ValueError("Descrição não pode estar vazia.")

    if amount <= 0:
        raise ValueError("Valor deve ser maior que zero.")

    if not category.strip():
        raise ValueError("Categoria não pode estar vazia.")

    return Expense(
        description=description.strip(),
        amount=round(amount, 2),
        category=category.strip(),
    )