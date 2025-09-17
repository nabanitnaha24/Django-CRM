import MySQLdb

# Connect to MySQL
dataBase = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Nabz@phewMYS24"
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE eldercooo")

print("All Done!")

# Close connection
dataBase.close()
