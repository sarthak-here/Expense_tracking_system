# Expense Tracking System

A full-stack expense tracking app with a FastAPI backend and Streamlit frontend, backed by MySQL.

## Features

- Log daily expenses with amount, category, and notes
- View expenses for any date
- Analytics: category-wise spending breakdown with percentages over a date range

## Tech Stack

- **Backend**: FastAPI, MySQL (via `mysql-connector-python`), Uvicorn
- **Frontend**: Streamlit
- **Testing**: pytest

## Project Structure

```
Expense_tracking_system/
├── Backend/
│   ├── server.py        # FastAPI app and route handlers
│   ├── db_helper.py     # MySQL query functions
│   └── logging_setup.py # Logger configuration
├── Frontend/
│   └── app.py           # Streamlit UI
└── tests/
    └── Backend/
        └── test_db_helper.py
```

## Setup

### Prerequisites

- Python 3.10+
- MySQL running locally with a database named `expense_manager`

### Database

Create the required table:

```sql
CREATE DATABASE expense_manager;

USE expense_manager;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    notes VARCHAR(255)
);
```

### Install Dependencies

```bash
pip install fastapi uvicorn mysql-connector-python streamlit requests
```

## Running the App

### 1. Start the Backend

```bash
cd Backend
uvicorn server:app --reload
```

Backend runs at `http://localhost:8000`.

### 2. Start the Frontend

```bash
cd Frontend
streamlit run app.py
```

Frontend runs at `http://localhost:8501`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/expenses/{date}` | Fetch all expenses for a date |
| POST | `/expenses/{date}` | Add expenses for a date |
| POST | `/analytics/` | Get category breakdown for a date range |

### Analytics Request Body

```json
{
  "start_date": "2024-08-01",
  "end_date": "2024-08-31"
}
```

## Running Tests

```bash
pytest tests/
```
