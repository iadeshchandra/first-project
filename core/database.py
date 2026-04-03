import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        tables = {
            "users": "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL);",
            "members": "CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, user_id INTEGER, membership_date TEXT, FOREIGN KEY(user_id) REFERENCES users(id));",
            "donations": "CREATE TABLE IF NOT EXISTS donations (id INTEGER PRIMARY KEY, member_id INTEGER, amount REAL, donation_date TEXT, FOREIGN KEY(member_id) REFERENCES members(id));",
            "expenses": "CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, amount REAL, description TEXT, expense_date TEXT);",
            "expense_items": "CREATE TABLE IF NOT EXISTS expense_items (id INTEGER PRIMARY KEY, expense_id INTEGER, item_name TEXT, cost REAL, FOREIGN KEY(expense_id) REFERENCES expenses(id));",
            "logs": "CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, action TEXT, log_date TEXT);"
        }

        for table in tables:
            self.cursor.execute(tables[table])

    def add_user(self, username, password):
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.connection.commit()

    def add_member(self, user_id, membership_date):
        self.cursor.execute('INSERT INTO members (user_id, membership_date) VALUES (?, ?)', (user_id, membership_date))
        self.connection.commit()

    def add_donation(self, member_id, amount, donation_date):
        self.cursor.execute('INSERT INTO donations (member_id, amount, donation_date) VALUES (?, ?, ?)', (member_id, amount, donation_date))
        self.connection.commit()

    def add_expense(self, amount, description, expense_date):
        self.cursor.execute('INSERT INTO expenses (amount, description, expense_date) VALUES (?, ?, ?)', (amount, description, expense_date))
        self.connection.commit()

    def add_expense_item(self, expense_id, item_name, cost):
        self.cursor.execute('INSERT INTO expense_items (expense_id, item_name, cost) VALUES (?, ?, ?)', (expense_id, item_name, cost))
        self.connection.commit()

    def log_action(self, action):
        self.cursor.execute('INSERT INTO logs (action, log_date) VALUES (?, ?)', (action, sqlite3.datetime.datetime.now()))
        self.connection.commit()

    def close(self):
        self.connection.close()