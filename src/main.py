import json
from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from pydantic import BaseModel
from fastapi.logger import logger as fastapi_logger
from logging.handlers import RotatingFileHandler
import logging
import pandas as pd
import pickle
import numpy as np

with open('./pipeline/models/iris_predict.pkl', 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s", "%Y-%m-%d %H:%M:%S")
handler = RotatingFileHandler('./src/logs/api.log', backupCount=0)
logging.getLogger().setLevel(20) # DEBUG 10, INFO 20, error 40
fastapi_logger.addHandler(handler)
handler.setFormatter(formatter)


class DataToPredict(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictOutput(BaseModel):
    predicted: int


@app.post("/predictions/",
          response_model=PredictOutput,
          responses={
              "200": {
                  "description": "Successful Response",
                  "content": {
                      "application/json": {
                          "example": {
                              "predicted": [
                                  {2.0},
                              ]
                          }
                      }
                  }
              }
          })
def predict(data: DataToPredict):
    """
        ADD DOC...
    """
    data = dict(data)
    with open(f'./src/tests/data.json', 'w') as jsonfile:
        json.dump(data, jsonfile)

    data = np.array(list(data.values())).reshape(1, -1)
    pred = model.predict(data)[0]

    fastapi_logger.info(f'{data}; predicted class : {pred} ')

    return {'predicted': pred}
