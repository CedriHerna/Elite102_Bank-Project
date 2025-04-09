import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'example', password = 'TsubasaNaru2-/11')

cursor = connection.cursor()

testQuery = ('SELECT * FROM student')

cursor.execute(testQuery)

for item in cursor:

    print(item)

cursor.close()

connection.close()

# First need to have a introduction of my Banking System.

# Make a log in to the bank and tell the user what
# type of access they have.

# IF THE USER IS NOT AN ADMIN
# Functions:

# Accounts: 

#   Manage account: 

#       Check Balance

#       Deposit

#       Withdraw


# IF THE USER IS AN ADMIN

# Functions:

# List of Users and their info

# Modify / Close any account

#       NAME | PIN | ADDRESS | SSN

# Add account