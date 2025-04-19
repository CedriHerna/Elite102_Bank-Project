import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'perico\'s_banking_system', password = 'TsubasaNaru2-/11')

cursor = connection.cursor()

# testQuery = ('SELECT Full_Name FROM list_of_users')

# cursor.execute(testQuery)

# for i, item in enumerate(cursor, start = 1):

#     string = (f'{item}')
#     remove_chars = "(),'"
#     translation_table = str.maketrans('', '', remove_chars)
#     text_filtered = string.translate(translation_table)
#     print(f'{i}. {text_filtered}')


# //// Admin Keys \\\\
# AdminUsername = "AdminUser"
# AdminPassword = "AdminPass"

# # //// Normal User Keys \\\\
# UserUsermane = "UserUser"
# UserPassword = "UserPass"




# First need to have a introduction of my Banking System.

# Make a log in to the bank and ask the user what
# type of access they have.



choices_for_admin = ["User List", "A user's account details", "Add an account", "Remove an account", "Quit"]





#                           //// Admin Functions \\\\
# IF THE USER IS AN ADMIN

# Functions:

# List of Users
def User_List():

    print("\n")

    listOfUsers = ('SELECT Full_Name FROM list_of_users')

    cursor.execute(listOfUsers)
    
    print("All users:")
    for item in cursor:
        
        string = (f'{item}')
        remove_chars = "(),'"
        translation_table = str.maketrans('', '', remove_chars)
        text_filtered = string.translate(translation_table)
        print(f'{text_filtered}')
    
    print("\n")

    # Account details

# Modify
#       NAME | PIN | ADDRESS | SSN

def specific_account_details():
    
    User_List()
    name = input("Who's account information would you like to look at?  ")
    
    account_details = "SELECT * FROM list_of_users WHERE Full_Name = '" + name + "'"
    # print(account_details)
    cursor.execute(account_details)

    # Pull out the query's results
    while(True):

        try:
            for item in cursor:
                
                string = (f'{item}')
                remove_chars = "()'"
                translation_table = str.maketrans('', '', remove_chars)
                text_filtered = string.translate(translation_table)
                array_of_details = text_filtered.split(", ")

            counter = 0
            for detail in array_of_details:
                if(counter == 0):
                    print(f'Full name: {detail}')
                elif(counter == 1):
                    address = detail
                    print(f'Address: {detail}')
                elif(counter == 2):
                    pin = detail
                    print(f'Pin: {detail}')
                elif(counter == 3):
                    SSN = detail
                    print(f'SSN: {detail}')
                counter += 1

            yesNo = input("Would you like to modify their information? (Y for yes, N for no)  ").upper()
    
            while(yesNo not in ('Y', 'N')):
                yesNo = input("Please try again. Y for yes, N for no.").upper()

            if(yesNo == 'N'):
                return Main_Page()
            
            option = input("Would you like to change the Name (Type '1'), Address (Type '2'), Pin (Type '3'), or SSN (Type '4')?  ")
            while(option not in ('1', '2', '3', '4')):
                option = input("Please try again.")

            breakpoint()
            while(True):

                if(option == '1'):
                    
                    newName = input("Please enter the new name you want to give this user.  ")
                    nameQuery = "UPDATE list_of_users SET Full_Name = '" + newName + "' WHERE Full_Name = '" + name + "'"
                    cursor.execute(nameQuery)
                    connection.commit()

                    print("Name Updated!")
                    option = input("Would you like to modify something else? Yes (Y) or No (N)?").upper()
                    while(option not in ('Y', 'N')):
                        option = input("Try again.").upper()
                    
                    if(option == 'N'):
                        return Main_Page()
                     
                elif(option == '2'):

                    newAddress = input("Please enter the new address you want to give this user.  ")
                    addressQuery = "UPDATE list_of_users SET Address = '" + newAddress + "' WHERE Address = '" + address + "'"
                    cursor.execute(addressQuery)
                    connection.commit()

                    print("Address Updated!")
                    option = input("Would you like to modify something else? Yes (Y) or No (N)?").upper()
                    while(option not in ('Y', 'N')):
                        option = input("Try again.").upper()
                    
                    if(option == 'N'):
                        return Main_Page()
                    
                elif(option == '3'):
                
                    newPin = input("Please enter the new pin you want to give this user.  ")
                    pinQuery = "UPDATE list_of_users SET Pin = '" + newPin + "' WHERE Pin = '" + pin + "'"
                    cursor.execute(pinQuery)
                    connection.commit()

                    print("Pin Updated!")
                    option = input("Would you like to modify something else? Yes (Y) or No (N)?").upper()
                    while(option not in ('Y', 'N')):
                        option = input("Try again.").upper()
                    
                    if(option == 'N'):
                        return Main_Page()

                elif(option == '4'):

                    newSSN = input("Please enter the new SSN you want to give this user.  ")
                    SSNQuery = "UPDATE list_of_users SET SSN = '" + newSSN + "' WHERE SSN = '" + SSN + "'"
                    cursor.execute(SSNQuery)
                    connection.commit()

                    print("Pin Updated!")
                    option = input("Would you like to modify something else? Yes (Y) or No (N)?").upper()
                    while(option not in ('Y', 'N')):
                        option = input("Try again.").upper()
                    
                    if(option == 'N'):
                        return Main_Page()

                option = input("What would you like to modify? Name (Type '1'), Address (Type '2'), Pin (Type '3'), or SSN (Type '4')?")
                while(option not in ('1', '2', '3', '4')):
                        option = input("Try again.")

        except:

            name = input("Please try again or press q to quit:  ")
            if(name == 'q'):
                break
            
            account_details = "SELECT * FROM list_of_users WHERE Full_Name = '" + name + "'"
            # print(account_details)
            cursor.execute(account_details)
    
    # Modify

    #       NAME | PIN | ADDRESS | SSN

    # Add account

    # Delete accounts

# Add account

def Add_Account():

    new_account_name = input("What is the name of this new user?   ")
    new_account_address = input(f"What is {new_account_name}'s address?   ")
    new_account_pin = input(f"What will {new_account_name}'s pin code be?   ")
    new_account_SSN = input(f"What is {new_account_name}'s Social Security Number?   ")
    
    new_username = input("What will be their username?   ")
    new_password = input("What will be their password?   ")
    
    # print('INSERT INTO list_of_users (Full_Name, Address, Pin, SSN) VALUES (\''+ new_account_name + '\', \'' + new_account_address + '\', \'' + new_account_pin +'\', \'' + new_account_SSN + '\')')
    
    new_user_query = ('INSERT INTO list_of_users (Full_Name, Address, Pin, SSN) VALUES (\''+ new_account_name + '\', \'' + new_account_address + '\', \'' + new_account_pin +'\', \'' + new_account_SSN + '\')')
    cursor.execute(new_user_query)
    connection.commit()

    new_login_query = ('INSERT INTO login (Login_Type, Username, Password, Full_Name) VALUES (\'User\', \'' + new_username + '\', \'' + new_password + '\', \'' + new_account_name + '\')')
    cursor.execute(new_login_query)
    connection.commit()

    print(f"User {new_account_name} successfully added!")

# Delete accounts

def Remove_Account():    
    # print("Remove account coming soon!")
    User_List()

    removed_user_name = input("Which user would you like to remove?   ")

    delete_login_query = (f"DELETE FROM login WHERE Full_Name = '{removed_user_name}'")
    cursor.execute(delete_login_query)
    connection.commit()

    delete_user_query = (f"DELETE FROM list_of_users WHERE Full_Name = '{removed_user_name}'")
    cursor.execute(delete_user_query)
    connection.commit()

    print(f"User {removed_user_name} successfully removed!")

#                            //// User Functions \\\\

#                           //// Shared Functions \\\\

def Login():

    global login_type

    print("Welcome to Perico's Banking System")

    login_type = input("Are you an admin or a normal user? (A for admin, U for User)\n").upper()

    while(login_type not in ('A', 'U')):

        login_type = input("Try again.").upper() 

    print("Please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")

def Main_Page():
    
    global counter
    global choice
    global double_return

    counter = 0
    double_return = False
    print("\n")

    if(login_type == 'A'):
        if(counter == 0):
            print("Welcome Admin. Please type in the number of the option you would like to select.")
            counter += 1
        else:
            print("Please type in the number of the option you would like to select.")

        for i, choice in enumerate(choices_for_admin, start = 1):
            print(f"{i}. {choice}")

        choice = input("")
        

        while(True):
            
            if(choice == "1"):
                User_List()
            elif(choice == "2"):
                specific_account_details()
                double_return = True
            elif(choice == "3"):
                Add_Account()
            elif(choice == "4"):
                Remove_Account()
            elif(choice == "5"):
                break
            else:
                choice = input("Please try again.   ")

            if(double_return == False):

                print("Please type in the number of the option you would like to select.")
                for i, choice in enumerate(choices_for_admin, start = 1):
                    print(f"{i}. {choice}")
                
                choice = input("")

            double_return = False

    elif(login_type == 'U'):

        print("UserSttufff")


# IF THE USER IS NOT AN ADMIN
# Functions:


#   Manage account: 

#       Check Balance

#       Deposit

#       Withdraw

#       Account Transations

#   Create New Account

#   Delete account


#                   //// Function call list \\\\

Login()
Main_Page()
cursor.close()
connection.close()
print("Thank you for choosing us. Have a great day!")