#pip install

#python3 -m venv (name of your project)     then we:   . venv/bin/activate

import requests

url = 'http://(whatever the link is)'

res = requests.get(url).json()

print(res)