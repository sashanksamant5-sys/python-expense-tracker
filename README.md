# Python Expense Tracker

A command-line expense tracker built with Python, migrated from JSON storage to PostgreSQL.

---

## Versions

### Version 1 — JSON (main branch)
The original version stores data in a local JSON file. Built as an early project to practice Python basics like functions, loops, file handling, and input validation.

### Version 2 — PostgreSQL (postgres branch)
An upgraded version that replaces JSON with a proper relational database. Introduces schema design, normalization, foreign keys, and SQL queries via psycopg2.

---

## Features
- Add expenses with category selection
- View all recorded expenses
- Calculate total expenses
- Delete expenses by ID
- Data persists across sessions

---

## Database Schema (Version 2)

**categories**
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Auto-generated ID |
| name | VARCHAR(100) | Category name (unique) |

**expenses**
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Auto-generated ID |
| amount | NUMERIC(10,2) | Expense amount |
| created_at | TIMESTAMP | Date and time of expense |
| category_id | INTEGER | Foreign key to categories |

---

## Technologies Used
- Python
- PostgreSQL
- psycopg2

---

## How to Run (Version 2)

1. Clone the repository and switch to the postgres branch:
```bash
git clone https://github.com/sashanksamant5-sys/python-expense-tracker.git
cd python-expense-tracker
git checkout postgres
```

2. Install dependencies:
```bash
pip install psycopg2-binary
```

3. Create a PostgreSQL database named `expensedb` and run the following SQL:
```sql
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    amount NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    category_id INTEGER REFERENCES categories(id)
);
```

4. Update your credentials in `database.py` and run:
```bash
python expense_tracker.py
```

---

## What I Learned
- Why relational databases are better than flat file storage
- How to normalize data using separate tables
- What foreign keys are and how they work
- How to connect Python to PostgreSQL using psycopg2
- How to use Git branches to manage different versions of a project

---

## Author
Sashank Samant