# import csv

import csv

field_names = ['name', 'age']
data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
    {'name': 'Emily', 'age': 33},
    {'name': 'Ashton', 'age': 59},
    {'age': 72, 'name': 'Paul'},
]
with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)

    ### Parsing means taking a stream of text and breaking it into meaningful chunks.
    # It is a vital process in turning code written in some source code language into executable code that can be made to perform some task on a computer.
