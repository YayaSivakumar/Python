# what_is_my_type.py
# Yachitra Sivakumar, 121373093

def type_of_variable(question):
    '''
    determines type of variable
    returns the variable and the variables type
    returns id of the variable
    '''
    my_type = type(question)
    return print("The variable is", question, "it is of type", my_type, "and has and id of", id(my_type))

type_of_variable(9)





