#this file is a module with a collection of functions, any function that does SQL stuff goes here
import mysql.connector as mysql

#function to connect to database, replace the password with whatever you have
def ConnectToDB(_host = "localhost",_user = "root",_database = "",_pass = "MYSQL123A",):
    db = mysql.connect(
    host = _host,
    user = _user,
    passwd = _pass,
    database = _database
    )

    print(db)
    print("Connection Established Successfully To:", _database)
    return db

#Creates a table for us
def InitTable(datab, TableName = 'PasswordDB'):
    cursor = datab.cursor()
    query = "CREATE TABLE IF NOT EXISTS" + " " + TableName + " (S_NO INT(5) PRIMARY KEY, UserID VARCHAR (20), Password VARCHAR (10), WebsiteURL VARCHAR(10))"
    cursor.execute(query);
    print("Table Initialized!");

#returns last ID of element inserted to prevent unique ID errors
def returnlastID(datab):
    cursor = datab.cursor()
    cursor.execute("SELECT * FROM PasswordDB")
    rows = cursor.fetchall()
    listofids = []

    for r in rows:
        listofids.append(r[0])

    if(len(listofids)) != 0:
        lastID = listofids[-1]
        return lastID;
    else:
        return 0
    
#This function takes in input for inserting values into the table
def InsertUserNamePass(datab, Username = "user", Password = "pass", _Website = "website",SNO = 0):
    cursor = datab.cursor()

    try:
        # Parameterized query
        sql_query = " INSERT INTO PasswordDB (S_NO,UserID, Password,WebsiteURL) VALUES (%s,%s,%s,%s)"
        # tuple to insert at placeholder
        values = (SNO,Username, Password, _Website)
        cursor.execute(sql_query, values)
        datab.commit()

        print("Data inserted successfully")

    except mysql.Error as error:
        print("parameterized query failed {}".format(error))

    

#for chirag to do
#this function should remove username AND password
def RemoveUserNamePass(datab, S_No_ToDelete = 1):
    #this method should work the same as the function above
    #Use Parameterized Query method from the function above
    #the sql query to delete is 'DELETE FROM TABLENAME WHERE CONDITION
    #HERE THE CONDITION SHOULD "S_NO == S_NO_ToDelete"

    cursor = datab.cursor()
    #display all records first so the user can know which row to delete
    FetchAllRecordsFromTable(datab)
    print(" ")
    S_No_ToDelete = int(input("Enter S.No To Delete Username & Password: "))
    sql_query = "DELETE FROM PasswordDB WHERE S_NO = {}".format(S_No_ToDelete)

    try:
        cursor.execute(sql_query)
        datab.commit()
        print("Data Deleted successfully")
    except mysql.Error as error:

        print("parameterized query failed {}".format(error))

        

def FetchAllRecordsFromTable(datab):
    cursor = datab.cursor()
    #use fetch all and equate that to a variable
    #then use for loop on that variable and print inside the for loop
    cursor.execute("SELECT * FROM PasswordDB")
    rows = cursor.fetchall()

    for r in rows:
        print(" ")
        print("Username: ", r[1])
        print("Password: ", r[2])
        print("Website URL: ", r[3])
        print(" ")


   
