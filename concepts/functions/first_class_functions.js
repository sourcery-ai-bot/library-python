```
Source: # == > https://www.youtube.com/watch?v=kr0mpwqttM0

A programming language is said to have first-class functions if it treats
functions as first class citizens.

A first-class citizen (sometimes called first-class objects) in a
programming language is an entity which supports all of the operations generally
available to other entities.These operations typically include being passed
as an argument, returned from a function, and assigned to a variable.```

function html_tag(tag) {
    function wrap_text(msg) {
        console.log('<' + tag + '>' + msg + '</' + tag + '>')
    }
    return wrap_text
}

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headlines!')

print_p = html_tag('p')
print_p('Test Paragraph!')
