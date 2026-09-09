"""#Multiple of Both 3 and 5
num = int(input("Enter the number:"))

if num %3 == 0 and num %5 == 0:
    print("The number "+ str(num) +" is multiple by both 3 and 5")
else:
    print("They are not multiple of both numbers")"""

#Password Checker
stored_password = "uii465koho"
user_password = input("Enter the password:")

if user_password == stored_password:
    print("Login successful")
else:
    print("Password is incorrect")
