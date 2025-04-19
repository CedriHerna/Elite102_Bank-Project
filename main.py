import mysql.connector
import tkinter as tk

#                           //// Tkinter functions \\\\
# root = tk.Tk()
# root.title("Perico's Banking System")

# title_label = tk.Label(root, text="Login")
# username_Label = tk.Label(root, text="Username")
# username_entry = tk.Entry(root)
# password_Label = tk.Label(root, text="Password")
# password_entry = tk.Entry(root, show="*")
# login_button = tk.Button(root, text="Login")

# title_label.grid(row=0,column=0, columnspan=2)

# username_Label.grid(row=2,column=0)
# username_entry.grid(row=2,column=1)
# password_Label.grid(row=3,column=0)
# password_entry.grid(row=3,column=1)
# login_button.grid(row=3,column=0, columnspan=2)




#                       //// mysql Connection and Cursor \\\\
connection = mysql.connector.connect(user = 'root', database = 'perico\'s_banking_system', password = 'TsubasaNaru2-/11')
cursor = connection.cursor()



#                           //// Admin Functions \\\\
# IF THE USER IS AN ADMIN
# Functions:

choices_for_admin = ["User List", "A user's account details", "Add an account", "Remove an account", "Quit"]

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

choices_for_user = ["Manage Account", "Quit"]

# IF THE USER IS NOT AN ADMIN
# Functions:

# Manage account: 
def Manage_Account():
    
    quit = True
    choices = ["Check Balance", "Deposit", "Withdraw", "Quit"]

    balance_query = (f"SELECT Balance FROM list_of_users WHERE Full_Name = '{Full_Name}'")
    cursor.execute(balance_query)
    for balance in cursor:
        balance = f'{balance}'
        remove_chars = "()',"
        translation_table = str.maketrans('', '', remove_chars)
        balance = balance.translate(translation_table)

    while(True):

        print("Type in the number of the option you would like to select.")
        for i, choice in enumerate(choices, start = 1):
            print(f"{i}. {choice}")
        choice = input("")

        while(choice not in ('1', '2', '3', '4')):
            choice = input("Try again.")

    #       Check Balance
        if(choice == '1'):

            print(f"Your balance currently is: ${balance}")
        elif(choice == '2'):

            deposit = input("How much are you depositing?   ")
            while(True):
                try:
                    deposit = float(deposit)
                    break
                except:
                    deposit = input("Please enter a number   ")
            
            balance = float(balance) + deposit
            deposit_query = (f"UPDATE list_of_users SET Balance = '{balance}' WHERE Full_Name = '{Full_Name}'")
            cursor.execute(deposit_query)
            connection.commit()
            print("Deposit complete!")

        elif(choice == '3'):

            withdraw = input('How much are you withdrawing?   ')
            while(True):
                try:
                    withdraw = float(withdraw)
                    break
                except:
                    withdraw = input("Please enter a number   ")

            if(float(balance) < withdraw):
                print(f'You do not have enough money in the account to withdraw that quantity. Current Balance: ${float(balance)}')

            else:
                balance = float(balance) - float(withdraw)
                withdraw_query = (f"UPDATE list_of_users SET Balance = '{balance}' WHERE Full_Name = '{Full_Name}'")
                cursor.execute(withdraw_query)
                connection.commit()
                print("Withdraw Complete!")
            
        elif(choice == '4'):
            cursor.fetchall()
            break
#                           //// Shared Functions \\\\

def Login():

    global login_type
    global Full_Name
    

    print("Welcome to Perico's Banking System")

    login_type = input("Are you an admin or a normal user? (A for admin, U for User)\n").upper()

    while(login_type not in ('A', 'U')):

        login_type = input("Try again.").upper() 

    print("Please enter your username and password")

    username = input("Username: ")
    password = input("Password: ")
    

    goodLogin = False
    
    while(goodLogin == False):

            if(login_type == "A"):
                admin_logins_query = ("SELECT Username, Password, Full_name FROM login WHERE Login_Type = 'Admin'")
                cursor.execute(admin_logins_query)
            else:
                user_logins_query = ("SELECT Username, Password, Full_name FROM login WHERE Login_Type = 'User'")
                cursor.execute(user_logins_query)

            for logins in cursor:

                stringLogins = (f'{logins}')
                remove_chars = "()'"
                translation_table = str.maketrans('', '', remove_chars)
                text_filtered = stringLogins.translate(translation_table)
                array_of_details = text_filtered.split(", ")

                if(array_of_details[0] == username and array_of_details[1] == password):
                    goodLogin = True
                    Full_Name = f"{array_of_details[2]}"
                    cursor.fetchall()
                    break
            
            if(goodLogin):
                break
            
            print("Please enter your username and password again.")

            username = input("Username: ")
            password = input("Password: ")
            usernamePassword = f"('{username}', '{password}')"

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

        if(counter == 0):
            print("Welcome User. Please type in the number of the option you would like to select.")
            counter += 1
        else:
            print("Please type in the number of the option you would like to select.")

        for i, choice in enumerate(choices_for_user, start = 1):
            print(f"{i}. {choice}")

        choice = input("")
      
        while(True):
            
            if(choice == "1"):
                Manage_Account()
            elif(choice == "2"):
                break
            else:
                choice = input("Please try again.   ")

            if(double_return == False):

                print("Please type in the number of the option you would like to select.")
                for i, choice in enumerate(choices_for_user, start = 1):
                    print(f"{i}. {choice}")
                
                choice = input("")

            double_return = False

        

#                          //// Function call list \\\\

Login()
Main_Page()
cursor.close()
connection.close()
print("Thank you for choosing us. Have a great day!")
# root.mainloop()