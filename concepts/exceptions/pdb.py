# The pdb module enables debugging

import pdb

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = 'Third'
result += third