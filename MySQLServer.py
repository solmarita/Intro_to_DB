import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

mycursor = mydb.cursor()

# Execute SQL statements using the execute() method on the cursor

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")
except:
    print("Failed to connect to DB!")

# Close connection to the databasse 
 
mycursor.close()
mydb.close()