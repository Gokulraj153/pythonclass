stored_user = "Gokul"
stored_password = "logout@123"

username = input("Enter the username: ")
password = input("Enter the Password:")

match (username,password):
    case username,password if username == stored_user and password == stored_password:
        print("Login Successful")
    case username,password if username != stored_user or password != stored_password:
        print("username or password is Invalid")
    case username,password if username == "" or password == "":
        print("username or password is not entered")
    
        
