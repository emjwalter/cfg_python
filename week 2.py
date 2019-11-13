# Homework from week 2

# Array of films

#film_list = variable

film_list = []

print(type(film_list))

film_list = ['The Snowman', 'Matilda', 'Harry Potter', 'Titanic', 'Home Alone', 'Official Secrets', 'Toy Story', 'Elf',
             'Monsters Inc.', 'Chicken Run']

selected_item = film_list[2]
print(selected_item)

print(film_list[0])
print(film_list[2])
print(film_list[6])
print(film_list[8])
print(film_list)

# to change the variable use the equals sign

film_list[2] = 'The Lion King'

print(film_list)

user_input = input('What is your favourite film?')
film_list[2] = user_input
print(film_list[2])

# print every element in my list
for film in film_list:
    print(film)

# you need to add 'str' to convert a number to a string (b/c Py doesn't like mixing types)
count = 1
for film in film_list:
    print(str(count) + ' - ' + film)
    count = count + 1

# If statements

user_input = input('How is the weather today?').strip()


if user_input == 'sunny':
    print('take your shorts!')
elif user_input == 'stormy':
    print('take rain coat')
elif user_input == 'rainy':
    print('take your umbrella')
elif user_input == 'rainy and stormy':
    print('stay home')
else:
    print("sorry, I didn't quite catch that")

