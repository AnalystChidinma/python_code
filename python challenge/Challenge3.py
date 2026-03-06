# check if a user email is not empty, contain @, and ends with '.com'

user_email = input("Enter your email: ")

if user_email is not None and "@" in user_email and user_email.endswith ('.com'):
    print (f"vaild email")
else:
    print(f"write a proper email that contain @ and ends with .com")
