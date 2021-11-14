# FastAPI Template

This is a basic template of FastAPI. The App can also be deployed on docker (cf [Docker](#Docker-run)).

The App predicts the class of the iris dataset.

## Getting started

**Important**: Once you clone the project, all the following commands have to be executed from the root directory of the project. If you have any troubles don't hesitate to reach me at : [anas.rabhi.hakim@gmail.com]() or [my linkedin](https://www.linkedin.com/in/anasrabhi/)

### Local run
***Warning** : If you are using python 32-bit it may not work. Use docker instead, or go to src -> main.py and rename `iris_predict.pkl` into `iris_predict_32b.pkl`*

Install all package in *requirements.txt*
````shell
pip install -r requirements/api_requirements.txt
````

Then run the server with : 

````shell
uvicorn src.main:app
````

or 

````shell
python src/main_local.py
````
Once the API is running you can send requests --> [How to send requests](#API-testing)

For more information visit : https://fastapi.tiangolo.com/

### Docker run
Use the *docker-compose.yml* file to build the container and run the App inside using the following
command : 
````shell
docker-compose up
````
Once the container is running you can send requests --> [How to send requests](#API-testing)

For more information about Docker visit: https://www.docker.com/resources/what-container 

### API testing

#### Method 1 : Using the browser
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

url = "http://127.0.0.1:8000/predictions"
response = requests.get(url, data=json.dump(data))

print(f"Predicted class : {response.json()['predicted']}")

````

#### Method 3 : Using request_sender file.

Run `request_sender.py`.
````shell
python src/tests/request_sender.py
````
Then enter the required data.