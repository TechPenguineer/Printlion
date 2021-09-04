
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint

PORT_OPTIONS = ['127.0.0.1', 'localhost']

questions = [
    {
        'type': 'input',
        'name': 'port_to_sever',
        'message': 'What port do you want to serve the display on?',
     },
    {
        'type': 'list',
        'name': 'type_of_host',
        'message': 'What type of host would you like to use?',
        'choices': PORT_OPTIONS,
    }
]
answers = prompt(questions)
pprint(answers)