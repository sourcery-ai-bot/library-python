"""The code below demonstrates the use of first class functions. This was
described by Corey Schafer on his video about first class functions on
YouTube"""

# == > https://www.youtube.com/watch?v=kr0mpwqttM0

"First Class Functions"

""" A programming language is said to have first-class functions if it treats
functions as first class citizens."""

""" A first-class citizen (sometimes called first-class objects) in a 
programming language is an entity which supports all of the operations generally
available to other entities. These operations typically include being passed
as an argument, returned from a function, and assigned to a variable."""


def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}")

    # Notice the absence of parenthesis. I don't want to call the function
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline')
print_h1('Another Headline')

print_p = html_tag('p')
print_p('Test Paragraph')
