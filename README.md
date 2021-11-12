# FastAPI Template

This is a basic template of FastAPI. The App can also be deployed on docker (cf [Docker](#Docker runj)).

The App predicts the class of the iris dataset.

## How to use

### Local run
*Warning : If you are using python 64-bit it may not work. Use docker instead.*

Install all libraries in *requirements.txt*
````shell
pip install -r requirements.txt
````

Then run the server with : 

````shell
uvicorn src.main:app
````

or 

````shell
python src/main_local.py
````
Once the API is running you can send requests --> [Testing](#API test)

For more information visit : https://fastapi.tiangolo.com/

### Docker run
In progress

### API test

#### Method 1 : Using your navigator
Once the API is running go to : **http://127.0.0.1:8000/docs**

#### Method 2 : Using python

````python
import json
import requests

# Respect the following structure.
data = {
  "sepal_length": 5,
  "sepal_width": 1,
  "petal_length": 0,
  "petal_width": 1
}

url_local = "http://127.0.0.1:8000/predictions"
response_local = requests.get(url_local, data=json.dump(data))

url_docker = "http://127.0.0.1:8000/predictions"
response_docker = requests.get(url_docker, data=json.dump(data))

````

#### Method 3 : Using request_sender file.

Run `request_sender_local.py`.
````shell
python src/tests/request_sender_local.py
````