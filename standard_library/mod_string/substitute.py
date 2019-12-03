from string import Template
from random import choices

actions = ['run', 'walk', 'swim', 'jump']
landmarks = [
    'Big Ben',
    'the Hague',
    'Sydney Harbour Bridge',
    'the Shard',
    'the Gherkin',
    'Tower Bridge',
    'the Statue of Liberty',
]

# Create a Template class that has 'action' and 'landmark' placeholder variables
template_str = Template('The main aimed to $action past $landmark.')
template_str = template_str.substitute(
    action=choices(actions)[0],
    landmark=choices(landmarks)[0],
)
print(template_str)
