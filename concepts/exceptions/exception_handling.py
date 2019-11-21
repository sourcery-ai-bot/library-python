""" The 'try' part of the block is the condition(s) to test.

The 'except' part of the block will be executed if an exception is thrown.
Multiple levels of exceptions can be added to this. The most specific exceptions
should be written at the top with the most general being at the bottom. This is 
so the compiler tests, throws and returns those most specific exceptions first.

The 'else' part of the block is executed if an exception is not found.

The 'finally' part of the block will run in any case. A good use case for this
might be closing a database which should be closed down irrespective of whether
an error is thrown."""

try:
    f = open('testfile.txt')
except FileNotFoundError:
    print("An error has occurred")
    raise FileNotFoundError
else:
    print(f.read())
    f.close()
finally:
    print("This line will print in any case")
