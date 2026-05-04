import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger


logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection =mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='expense_manager'
    )
    if connection.is_connected():
        print("Connnection succesful")
    else:
        print("Failed in connecting to a database")
    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()
    
def fetch_all_records():
    logger.info("Fetching all records from the database")
    with get_db_cursor() as cursor:
        cursor.execute('SELECT * FROM expenses')
        expenses = cursor.fetchall()
        for expense in expenses:
            #print(expense)
            pass
        return expenses

def fetch_all_records_by_date(expense_date):
    logger.info(f"Fetching records for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute('SELECT * FROM expenses where expense_date =%s',(expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            #print(expense)
            pass
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Inserting expense for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute('INSERT INTO expenses (expense_date, amount , category, notes) VALUES (%s, %s, %s, %s)',
                       (expense_date, amount, category, notes)
                       )
def delete_expense_for_date(expense_date,amount, category , notes):
    logger.info(f"Deleting expense for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute('DELETE FROM expenses where expense_date = %s AND amount = %s AND category = %s AND notes = %s',
                       (expense_date, amount, category, notes))
        
def fetch_expense_summary(start_date, end_date):
    logger.info(f"Fetching expense summary from {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('SELECT category, SUM(amount) as total FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category',
                       (start_date, end_date))
        data = cursor.fetchall()
        return data
                       
if __name__ == "__main__":
    #fetch_all_records()
    #fetch_all_records_by_date('2024-08-20')
    #insert_expense('2024-08-20', 300, 'Food', 'pani puri')
    #fetch_all_records_by_date('2024-08-20')
    #delete_expense_for_date('2024-08-20', 300, 'Food', 'pani puri')
    #fetch_all_records_by_date('2024-08-20')
    #summmary = fetch_expense_summary('2024-08-01', '2024-08-31')
    #for record in summmary:
        #print(record)
    pass



