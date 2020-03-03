""" Returns a re.Match object if the tested_password has 8 or more characters with at
    least 1 number, 1 uppercase letter, 1 lowercase letter and one special character. 
    If the password is not valid, returns 'None'. """

import re

def check_password(p):
    return re.match(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,}$", p)

tested_password = check_password(p='Test1234!')
print('Password has failed') if tested_password is None else print('Password is OK')
