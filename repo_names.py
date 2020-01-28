import pandas as pd
import requests
import json


url = 'https://api.github.com/users/Gregistrar/repos'

r = requests.get(url)
data = r.json()

for i in data:
    print(i['name'])
