### pypi.org
## https://pypi.org/project/requests2/
# pip: A package manager used to install libraries that other people have written

# API
# application programming interface
# sends info from one dictionary to another  JSON

# sentimental analysis, machine reads the individual responses without the person needing to do so

import requests
from pprint import pprint

## Step1 build an URL ##

pokemon_number = input("What is the Pokemon's ID?")

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
print(url)

## Step2 - query URL (using request package)  -- if we don't want to lost something, store it in a variable ##

response = requests.get(url)
print(response)

response_dict = response.json()
print(response_dict)
