# bugs.py
# Yachitra Sivakumar, 121373093

'''
    initial thoughts
    first paragraph has an extra "'
    second paragraph needs ()
    third paragraph needs : and will return phrase 'a_parameter'
    forth paragraph is ok
    fifth paragraph needs , between first and second parameter
    sixth paragraph needs , in return line
'''

# I'm a comment
''' I'm a comment '''
''' I'm a comment '''
""" I'm a comment """
age = 7 # I'm a comment

def a_function(a_parameter):
    return a_parameter

def a_function(a_parameter):
    return "a_parameter"

def a_function(a_parameter, a_second_parameter):
    return a_parameter, a_second_parameter

a_function(3, 8)