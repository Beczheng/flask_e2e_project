import sqlite3
import pandas as pd

# Initialize the database
DATABASE = '/home/beckie_zheng/flask_e2e_project/app/users.db'

# Search for user in database
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# Get values from users table
df = pd.read_sql_query("SELECT * FROM users", db)