# check if a username is a string, is not none and is longer than 5 character

user_name = "adaeze234_"

if user_name is not None and isinstance (user_name, str) and len(user_name) > 5:
    print("user name is valid")
else:
    print("user name is invalid")