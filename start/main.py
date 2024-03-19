import psycopg2

connect = psycopg2.connect(
    database="sql-new", user="postgres", password="rest", host="127.0.0.1",
    port="5432"
)

cursor = connect.cursor()

cursor.execute('''alter table users add column numbers numeric''')

connect.commit()
print("Insert into users table")

# Closing the connection
connect.close()
