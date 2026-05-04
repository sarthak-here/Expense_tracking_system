from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel
from fastapi import HTTPException

class Expense(BaseModel):
    expense_date: date
    amount: float
    category: str
    notes: str   
class DateRange(BaseModel):
    start_date: date
    end_date: date
app = FastAPI()

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_all_records_by_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="No expenses found for the given date")
    
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    for expense in expenses:
        add = db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    if add is None:
        raise HTTPException(status_code=500, detail="Failed to add expenses")
    return {"message": "expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data =db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="No data found for the given date range")
    total = sum([row['total'] for row in data])
    breakdown = {}
    for row in data:
        percentage = (row['total'] / total) * 100 if total > 0 else 0
        breakdown[row['category']] = {
            'total': row['total'],
            'percentage': percentage
        }
    return breakdown