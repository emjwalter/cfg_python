# adding time to display results

import time

animals_list = [
{'species': 'zebra', 'name': 'Penelope'},
{'species': 'penguin', 'name': 'Jenn'},
{'species': 'elephant', 'name': 'Harris'},
{'species': 'flamingo', 'name': 'Florence'},
]

for animal in animals_list:
    print(animal)
    print(animal['species'])

    time.sleep(2)
