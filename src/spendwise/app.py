from .expenses import create_expense
from .storage import load_expenses, save_expenses

def show_menu() -> None:
    print("\n=== SpendWise CLI ===")
    print("1. Adicionar despesa")
    print("2. Listar despesa")
    print("3. Remover despesa")
    print("4. Exibir gastos totais")
    print("5. Exibir total por categoria")
    print("6. Sair")


def add_expense() -> None:
    description = input("Descrição: ")
    amount = float(input("Valor: "))
    category = input("Categoria: ")

    expenses = load_expenses()
    expenses.append(create_expense(description, amount, category))
    save_expenses(expenses)

    print("Despesa adicionada com sucesso!")


def list_expenses() -> None:
    expenses = load_expenses()

    if not expenses:
        print("Nenhuma despesa registrada.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense.description} - R${expense.amount:.2f} [{expense.category}]")


def remove_expense() -> None:
    expenses = load_expenses()
    list_expenses()

    if not expenses:
        return

    index = int(input("Digite o número de despesa para remover: "))

    if index < 1 or index > len(expenses):
        print("Número de despesa inválido.")
        return

    removed = expenses.pop(index - 1)
    save_expenses(expenses)

    print(f"Despesa removida: {removed.description}")


def show_total_spent() -> None:
    expenses = load_expenses()
    total = sum(expense.amount for expense in expenses)

    print(f"Gasto total: R${total:.2f}")


def show_total_by_category() -> None:
    expenses = load_expenses()
    totals: dict[str, float] = {}

    for expense in expenses:
        totals[expense.category] = totals.get(expense.category, 0) + expense.amount

    if not totals:
        print("Nenhuma despesa registrada.")
        return

    for category, total in totals.items():
        print(f"{category}: R${total:.2f}")


def main() -> None:
    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            add_expense()
        elif option == "2":
            list_expenses()
        elif option == "3":
            remove_expense()
        elif option == "4":
            show_total_spent()
        elif option == "5":
            show_total_by_category()
        elif option == "6":
            print("Adeus!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()