#Check if the password is atleast 8 characters long and does not contain spaces

password = input("Enter your password: ")

if len(password) >= 8 and " " not in password:
    print(f"password approved")
else:
    print (f"password must have atleast 8 character long and must not contain spaces")