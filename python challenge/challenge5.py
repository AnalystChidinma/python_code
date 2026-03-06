# check if the user is either an admin or adminstrator, and either they're not banned or they've verified their email.

user = "admin"
is_banned = True
email_verified = False

if user in ["admin", "administrator"] and (not is_banned or email_verified):
    print ("user Access Approve")
else:
    print("user access denial")