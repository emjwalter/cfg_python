# Define a list with 10 names!

register = ['Bob', 'Billy', 'Brenda', 'Betty', 'Brian', 'Barry', 'Belle', 'Bertie', 'Becky', 'Belinda']

# use a for loop to print out all the names in the following format:

# 1 - Welcome Angelo
# 2 - Welcome Monica
# (....)


register = ['Bob', 'Billy', 'Brenda', 'Betty', 'Brian', 'Barry', 'Belle', 'Bertie', 'Becky', 'Belinda']

count = 0   ## note to self: put the count before the block of code ##
edit_r_list = []
for name in register:
    # print(name)
    # print(count)
    print(str(count) + ' - Welcome ' + name)
    edit_r_list.append(str(count) + ' - ' + name)
    count = count + 1

# optional
print(edit_r_list)


# Sweet! Now do the same using a While loop

