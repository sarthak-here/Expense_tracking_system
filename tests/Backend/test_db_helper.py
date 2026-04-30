from Backend import db_helper
import os
import sys
print(__file__)

def test_fetch_all_records_by_date():
    expenses = db_helper.fetch_all_records_by_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == 'Shopping'
    assert expenses[0]['notes'] == "Bought potatoes"