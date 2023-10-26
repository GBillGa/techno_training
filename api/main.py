from typing import Union

from fastapi import FastAPI
from .nba_api_functions import get_games

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/games/{date_param}")
def return_games_from_date(date_param: str):
    return get_games(date_param)

@app.get("/games/")
def return_games_from_date():
    return get_games()
