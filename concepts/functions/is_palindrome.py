def is_palindrome(string):
    return string == string[::-1]

is_str_palindrome = is_palindrome('redivider')
print(f"{is_str_palindrome = }")
