""" Finds the domain name from the string """

string = 'From a.n.other@gmail.com Sun 17 Feb 2018 15:34'

# Solution 1
domain_name = string[string.find('@'): string.find(' ', string.find('@'))].strip()
print(f"{'Solution 1 Domain Name:'} {domain_name}")

# Solution 2
start_position = string.find('@')
end_position = string.find(' ', start_position)
domain_name = string[start_position: end_position].strip()
print(f"{'Solution 2 Domain Name:'} {domain_name}")

"""
# NOTE:
In the example above, the first method of resolving the issue is a more
tersely written expression, however since the zen of Python stipulates that
readability counts, then the more Pythonic approach would be the second one.

The .strip() method is not required as there is actually no leading or trailing
spaces, however it has been applied as a belt and braces approach to ensure
there is none.
"""
