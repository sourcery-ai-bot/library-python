import getpass

# The username can be received through standard input from the user
username = input('Username: ')

# The getpass function conceals the password entered
password = getpass.getpass('Password: ')

# The password entered is still printed here. It was just concealed
# from view in the previous step
print(f"The username is {username} and the password is {password}.")
