# what_is_my_name.py
# Yachitra Sivakumar, 121373093

'''
create variable for first name
ask input for users first name
create variable for second name
ask input for users second name
print back 'hello' followed by users input
'''

first_name = (input("Please insert your first name: "))
second_name = (input("Please insert your last name: "))

first_name_lower = first_name.lower()
second_name_lower = second_name.lower()

print("hello", first_name_lower.capitalize(), second_name_lower.capitalize())

print(first_name.partition())
