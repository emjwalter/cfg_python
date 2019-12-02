# Ask the user to input a new to-do item

todo_new = input("What's your new to do thing?")

# Read the contents of the existing to-do items

with open('todo.txt', 'r') as open_file:
    todo_items = open_file.read()

# Add the new to do item to the existing to-do items

update_todo = todo_items + todo_new

# Save the updated to-do items
with open ('todo.txt', 'w') as open_file:
open_file.write ##  this line is not finished

# ALTERNATIVE FIX from CF:G

new_item = input('Enter a to-do item: ')

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '\n'

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)

 # https://docs.python.org/3/library/functions.html#open

