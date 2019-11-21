def is_palindrome(string):
    return string == string[::-1]

is_str_palindrome = is_palindrome('LOL')
print(is_str_palindrome)
