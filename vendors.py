import mysql.connector as sqltor

# Connect to the database
conn = sqltor.connect(
    host='localhost',
    user='root',
    password='123456',  # Use straight quotes
    database='vendors'
)

if conn.is_connected():
    print('Successfully connected to MySQL database')
else:
    print("ERROR")

cursor = conn.cursor()

# Display all rows
cursor.execute("SELECT * FROM effects")
data = cursor.fetchall()
print("Total number of rows retrieved in result set:", len(data))
for row in data:
    print(row)

# Menu-driven program
print("""
CHOICES:
1. Add a new record in table effects
2. Search for a record in table effects
3. Delete an existing record from table effects
4. Alter the table effects
5. Update the table effects
6. Quit the program
""")

choice = int(input("Enter a choice (1,2,3,4,5,6): "))

# Define functions
def insert():
    particular = input("Enter a particular effect: ")
    prelockdown = int(input("Enter prelockdown number: "))
    lockdown = int(input("Enter lockdown number: "))
    postlockdown = int(input("Enter postlockdown number: "))
    query = "INSERT INTO effects VALUES (%s, %s, %s, %s)"
    values = (particular, prelockdown, lockdown, postlockdown)
    cursor.execute(query, values)
    conn.commit()
    print("New record inserted successfully")

def search():
    particular = input("Enter the particular effect to search: ")
    query = "SELECT * FROM effects WHERE particular = %s"
    cursor.execute(query, (particular,))
    results = cursor.fetchall()
    for row in results:
        print(row)

def delete():
    particular = input("Enter the particular effect to delete: ")
    query = "DELETE FROM effects WHERE particular = %s"
    cursor.execute(query, (particular,))
    conn.commit()
    print("Record deleted successfully")

def alter():
    column = input("Enter the column name to add: ")
    datatype = input("Enter the data type of the new column (e.g., VARCHAR(50)): ")
    query = f"ALTER TABLE effects ADD {column} {datatype}"
    cursor.execute(query)
    conn.commit()
    print("New column added successfully")

def update():
    particular = input("Enter the particular effect to update: ")
    prelockdown = int(input("Enter new prelockdown number: "))
    lockdown = int(input("Enter new lockdown number: "))
    postlockdown = int(input("Enter new postlockdown number: "))
    query = """
    UPDATE effects
    SET prelockdown = %s, lockdown = %s, postlockdown = %s
    WHERE particular = %s
    """
    values = (prelockdown, lockdown, postlockdown, particular)
    cursor.execute(query, values)
    conn.commit()
    print("Record updated successfully")

# Run choice
if choice == 1:
    insert()
elif choice == 2:
    search()
elif choice == 3:
    delete()
elif choice == 4:
    alter()
elif choice == 5:
    update()
elif choice == 6:
    print("Exiting from the program")
else:
    print("Invalid choice")

# Close the connection
cursor.close()
conn.close()
