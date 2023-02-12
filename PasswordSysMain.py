#we are calling our own module here
#we are using modules for code readability which is required for this project
#this is The Main python file where all the main functionality goes, menu and entering passwords and stuff

import SQLCommandModule as SQLLib;

#any function we call from our module we should pass this variable as the database so it can understand which database we are using
_DBMS = SQLLib.ConnectToDB(_database = "test")
#creates the table for storing usernames and passwords
SQLLib.InitTable(_DBMS)
print(" ")


print("------------------------")
print("1 - Insert Username & Password")
#2 to do by chirag
print("2 - Delete Username & Password")
#3 to do by sreeni
print("3 - Show Usernames & Passwords")
#4 done by me
print("4 - Exit Program")
print("------------------------")

#initialized the serial number of each username password
_SNO = 0
#we obtain the last serial number of the last entry we inserted into the table
#this is so that when we run the program again, it does not return to 0 and give us a unique id error due to matching primary keys
_SNO = SQLLib.returnlastID(_DBMS)

while True:
    print(" ")
    choice = input("Enter Choice: ")

    if choice == "1": 
        while True:
            print("------------------------")
            user = input("Enter Username: ")
            _pass =  input("Enter Password: ")
            _URL =  input("Enter WebsiteURl: ")
            _SNO += 1

            SQLLib.InsertUserNamePass(_DBMS,user,_pass,_URL,_SNO)

            print("Continue? (Y/N)")
            ch = input("Enter Choice: ")
            if(ch in ["y","Y"]):
                continue
            elif (ch in ["n","N"]):
                print("------------------------")
                break
            else:
                print("------------------------")
                break
    

    elif(choice == "2"):
        SQLLib.RemoveUserNamePass(_DBMS,_SNO)
    
    elif(choice == "3"):
        SQLLib.FetchAllRecordsFromTable(_DBMS)

    elif choice == "4":
        break

