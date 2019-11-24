# Dictionaries!

# Fine a dictionary with cool things inside!
    # Examples: Christmas list with item and price
    # complete the sentence:
    # Dictionaries are organised using: ___KEYS_??? and  _VALUES___?


# Print the dictionary and check it's type
presents = {'book': 'Harry Potter',
            'car': 'Audi',
            'gadget': 'radio',
            'transport': 'scooter',
            'device': 'laptop'}
print(presents)
print(type(presents))

# Print the dictionary keys
print(presents.keys())

# Print the dictionary's values
print(presents.values())

# Print the dictionary first key and value together
keys = list(presents.keys())
values = list(presents.values())

print(keys[0] + ' ' + (values [0]))

# Re-define the value on the dictionary using it's key
presents['device']='phone'
print(presents)

# Re-define another value on the dictionary using it's key
presents['transport'] = 'hovercraft'
print(presents)

# Add on a new key  - value to the dictionary (say rating)
presents['rating'] = '5stars'
print(presents)

# Access only the value of the last key you created from the dictionary
keys = list(presents.keys())
size = len(keys)
last_key = keys[size-1]
print(presents[last_key])

# Re-define that value in the dictionary
presents[last_key] = '3stars'
print(presents)