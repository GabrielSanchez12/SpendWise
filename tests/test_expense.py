from spendwise.expenses import create_expense

def test_create_valid_expense():
    expense = create_expense(
        description="Lanche",
        amount=25.50,
        category="Comida",
    )

    assert expense.description == "Lanche"
    assert expense.amount == 25.50
    assert expense.category == "Comida"


def test_create_expense_with_empty_description():
    try:
        create_expense(
            description="",
            amount=10,
            category="Comida",
        )
    except ValueError as error:
        assert str(error) == "Descrição não pode estar vazia."


def test_create_expense_with_negative_amount():
    try:
        create_expense(
            description="Uber",
            amount=-15,
            category="Transporte",
        )
    except ValueError as error:
        assert str(error) == "Valor deve ser maior que zero."