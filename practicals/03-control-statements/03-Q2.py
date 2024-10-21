new_password = input("Enter a new password: ")
check_password = input("Re-Enter the password: ")

new_password = str(new_password)
check_password = str(check_password)

if new_password == check_password:
    print("***Password set***")
else:
    print("Passwords entered do not match, please re-enter passwords and try again!")