# Writing to a file

# '+' = reading and writing

# using '\n' enters a new line


with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nAmina'
    text_file.write(people)


with open('dinner.txt', 'w+') as text_file:
    dinner = 'ribs \nLong Island Ice Tea \nnachos'
    text_file.write(people)