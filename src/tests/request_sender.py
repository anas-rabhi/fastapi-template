import sys
import requests
import json
import os

url = 'http://127.0.0.1:8000/predictions'

data = {}

for i in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:

    try:
        data[i] = float(input(f'{i} = '))
    except Exception:
        print(f"ERROR : Enter a number")
        for j in range(100):
            try:
                data[i] = float(input(f'{i} = '))
                break
            except Exception:
                print(f"Enter a number, try number : {j + 2}.")

response = requests.post(url, data=json.dumps(data))

if response.status_code == 200:
    print('request ok')
    prediction = response.json()['predicted']
    print('Predicted class : ', prediction)

    """
    if not os.path.isdir('./results'):
        os.mkdir('./results')
    prediction = {"prediction": prediction}
    with open(f'./src/test/predicted.json', 'w') as jsonfile:
        json.dump(prediction, jsonfile)
    """
else:
    print('request failed with code ', response.status_code)
