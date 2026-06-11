import os

from dotenv import load_dotenv
from supabase import Client, create_client

from .expenses import Expense


load_dotenv()


def get_supabase_client() -> Client:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("Supabase URL ou chave não configurados.")

    return create_client(url, key)


def load_expenses() -> list[Expense]:
    supabase = get_supabase_client()

    response = supabase.table("expenses").select("*").order("id").execute()

    return [
        Expense(
            id=item["id"],
            description=item["description"],
            amount=float(item["amount"]),
            category=item["category"],
        )
        for item in response.data
    ]


def save_expense(expense: Expense) -> None:
    supabase = get_supabase_client()

    supabase.table("expenses").insert(
        {
            "description": expense.description,
            "amount": expense.amount,
            "category": expense.category,
        }
    ).execute()


def delete_expense(expense_id: int) -> None:
    supabase = get_supabase_client()

    supabase.table("expenses").delete().eq("id", expense_id).execute()