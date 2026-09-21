dbemail = "useremail@gmail.com"
dbpassword = "logout@123"

useremail = input("Enter the User Email Id: ")
userpassword = input("Enter the Password: ")

if useremail != "" and userpassword != "":
    if dbemail == useremail:
        if dbpassword == userpassword:
            print("Login Successful")
        else:
            print("Password is not match, Enter the Valid Password")
    else:
        print("Email is not match, Enter the Valid Email id")

else:
    if useremail=="":
        print("Email is empty, Please enter the valid email id.")
    elif userpassword == "":
        print("Password is empty, Please enter the valid password.")
    else:
        print("Both Email and Password are empty,Please enter the valid email and password.")
