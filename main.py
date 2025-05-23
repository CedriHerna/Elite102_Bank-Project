import mysql.connector





#                       //// mysql Connection and Cursor \\\\
connection = mysql.connector.connect(user = 'root', database = 'perico\'s_banking_system', password = 'TsubasaNaru2-/11')  #This enables VSCode to access an SQL database.
cursor = connection.cursor()                                                                                               #This cursor allows the program to pull specific data out of the SQL database. 



#                           //// Admin Functions \\\\
# IF THE USER IS AN ADMIN
# Functions:

choices_for_admin = ["User List", "A user's account details", "Add an account", "Remove an account", "Quit"]
# This is an array that holds all the choices an admin can select.

# List of Users
def User_List():

    print("\n")

    listOfUsers = ('SELECT Full_Name FROM list_of_users')

    cursor.execute(listOfUsers)
    # collects data for the for loop to extract.
    print("All users:")
    for item in cursor:
        
        string = (f'{item}')
        remove_chars = "(),'"
        translation_table = str.maketrans('', '', remove_chars)
        text_filtered = string.translate(translation_table)
        print(f'{text_filtered}')                               #This for loop prints out all the users.
    
    print("\n")

    # Account details

# Modify
#       NAME | PIN | ADDRESS | SSN

def specific_account_details():
    
    User_List()
    name = input("Who's account information would you like to look at?  ")
    
    account_details = "SELECT * FROM list_of_users WHERE Full_Name = '" + name + "'"
    
    cursor.execute(account_details)

    # Pull out the query's results, which holds all the specific details of a specific user.
    while(True):

        try:
            for item in cursor:
                
                string = (f'{item}')
                remove_chars = "()'"
                translation_table = str.maketrans('', '', remove_chars)
                text_filtered = string.translate(translation_table)
                array_of_details = text_filtered.split(", ")
                # This places all of the full name, address, SSN, and pin information of a specific person in an array

            counter = 0
            for detail in array_of_details:   #This pulls the user's address, pin, and SSN for later use as well as displaying them.
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

            
            while(True):

                if(option == '1'):
                    
                    newName = input("Please enter the new name you want to give this user.  ")
                    nameQuery = "UPDATE list_of_users SET Full_Name = '" + newName + "' WHERE Full_Name = '" + name + "'"
                    cursor.execute(nameQuery)
                    connection.commit()
                    # Above updates the name within SQL
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
                    # Above updates the address within SQL
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
                    # Above updates the pin within SQL
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
                    # Above updates the SSN within SQL
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
                return Main_Page()
            
            
    
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
        
    new_user_query = ('INSERT INTO list_of_users (Full_Name, Address, Pin, SSN) VALUES (\''+ new_account_name + '\', \'' + new_account_address + '\', \'' + new_account_pin +'\', \'' + new_account_SSN + '\')')
    cursor.execute(new_user_query)
    connection.commit()

    new_login_query = ('INSERT INTO login (Login_Type, Username, Password, Full_Name) VALUES (\'User\', \'' + new_username + '\', \'' + new_password + '\', \'' + new_account_name + '\')')
    cursor.execute(new_login_query)
    connection.commit()

    print(f"User {new_account_name} successfully added!")

# Delete accounts

def Remove_Account():    

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

# Choice Functions which allow me to unit test.
def deposits(deposit, balance, Full_Name): 
    
    while(True):
        try:
            deposit = float(deposit)
        except:
            deposit = input("Please enter a number   ")
        
        balance = float(balance) + deposit
        if(Full_Name != 'j'):   #'j' is the Full_Name of the unit test
            deposit_query = (f"UPDATE list_of_users SET Balance = '{balance}' WHERE Full_Name = '{Full_Name}'")
            cursor.execute(deposit_query)
            connection.commit()
            print("Deposit complete!")
        return balance  #This is just for the unit test to analyze

def printBalance(balance):
    return f"Your balance currently is: ${balance}"
    

# Manage account: 
def Manage_Account():
    global balance
    choices = ["Check Balance", "Deposit", "Withdraw", "Quit"]
    
    balance_query = (f"SELECT Balance FROM list_of_users WHERE Full_Name = '{Full_Name}'")
    cursor.execute(balance_query)
    
    while(True):

        for balance in cursor:
            balance = f'{balance}'
            remove_chars = "()',"
            translation_table = str.maketrans('', '', remove_chars)
            balance = balance.translate(translation_table)

        print("Type in the number of the option you would like to select.")
        for i, choice in enumerate(choices, start = 1):
            print(f"{i}. {choice}")
        choice = input("")

        while(choice not in ('1', '2', '3', '4')):
            choice = input("Try again.")

    #       Check Balance
        if(choice == '1'):
            print(printBalance(balance))    #This calls a specific function and prints what it returns to show the user their balance
             
        elif(choice == '2'):

            deposit = input("How much are you depositing?   ")
            deposits(deposit, balance, Full_Name)                        #I added Full_Name so that my unit tests could work. However, for some reason by making this a function it doesn't update balance until you quit and then return.
                                                                         #if I just dropped the function here, it would update instantly.

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
                admin_logins_query = ("SELECT Username, Password, Full_name FROM login WHERE Login_Type = 'Admin'")  #Finds admin logins
                cursor.execute(admin_logins_query)
            else:
                user_logins_query = ("SELECT Username, Password, Full_name FROM login WHERE Login_Type = 'User'")    #Finds user logins
                cursor.execute(user_logins_query)

            for logins in cursor:

                stringLogins = (f'{logins}')
                remove_chars = "()'"
                translation_table = str.maketrans('', '', remove_chars)
                text_filtered = stringLogins.translate(translation_table)
                array_of_details = text_filtered.split(", ")                    #This splits up the username and password of the specific user on this iteration

                if(array_of_details[0] == username and array_of_details[1] == password):  #if it finds the right username and password, break out of the loop.
                    goodLogin = True
                    Full_Name = f"{array_of_details[2]}"
                    cursor.fetchall()                                               #This is here to empty the cursor so that the program can call the cursor again.
                    break
            
            if(goodLogin):
                break                                                                  #Breaks out the while loop if it finds the correct username/password OR asks for the user to enter their username/password again.
            
            print("Please enter your username and password again.")

            username = input("Username: ")
            password = input("Password: ")
            

def Main_Page():
    
    global counter
    global choice
    global double_return    #These are variables that must have a global scope as they are used in multiple parts of the program.

    counter = 0
    double_return = False
    print("\n")
    
    if(login_type == 'A'):

        if(counter == 0):
            print("Welcome Admin. Please type in the number of the option you would like to select.")
            counter += 1    #Makes sure I don't say welcome more than once.
        else:
            print("Please type in the number of the option you would like to select.")

        for i, choice in enumerate(choices_for_admin, start = 1):
            print(f"{i}. {choice}")

        choice = input("")
        

        while(True):
            # Pushes the user/admin to their respective choice.
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

            double_return = False   #Ensures that it doesn't ask to quit twice on the same page.

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

            double_return = False  #Ensures that it doesn't ask to quit twice on the same page.







#                          //// Function call list \\\\

Login()
Main_Page()
cursor.close()
connection.close()
print("\nThank you for choosing us. Have a great day!")
