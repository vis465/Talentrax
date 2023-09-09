import sqlite3
from tabulate import tabulate

# Create a SQL connection to the SQLite database
con = sqlite3.connect('db.sqlite3')

# Create a cursor
cur = con.cursor()

# Define the table name for users
user_table_name = 'courses_lesson'

# Execute a query to retrieve all users from the table
query = f"SELECT * FROM {user_table_name}"
cur.execute(query)

# Fetch all the rows
users = cur.fetchall()

# Get the column names from the cursor description
column_names = [desc[0] for desc in cur.description]

# Display user data in a tabular format
print(tabulate(users, headers=column_names, tablefmt="grid"))

# Close the connection
con.close()
'''
x=con.execute("SELECT * FROM sqlite_master where type='table'")

for y in x.fetchall():
    print(y)'''