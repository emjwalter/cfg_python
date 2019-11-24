# Lists!

# Define a list with cool things inside!
    # Examples: Christmas list, things you would buy with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: ___variables____?????


# Print the lists and check its type
dreams = ['mansion', 'horses', 'Mercedes', 'flowers', 'perfume']
print(dreams)
print(type(dreams))

# Print the list's first object
print(dreams[0])

# Print the list's second object
print(dreams[1])

# Print the list's last object   ### remember to include -1 at the end to find the last value in the list
print(dreams[len(dreams)-1])

# Re-define the first item on the list and
dreams[0] = 'chateau'
print(dreams)

# Re-define another item on the list and print all the list
dreams[2]= 'BMW'
print(dreams)

# Add an item to the list and print the list
dreams.append('husband')
print(dreams)

# Remove an item from the list and print the list
dreams.remove('horses')
print(dreams)

# Add two items to list and print the list
dreams.append('kitten')
dreams.append('garden')
print(dreams)