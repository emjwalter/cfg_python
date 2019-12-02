import csv

with open('trees.csv', 'r') as open_file:

spreadsheet = csv.DictReader(open_file)
# Add code to open the csv file

heights = []

for row in spreadsheet:
    tree_height = row['height']
    heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)