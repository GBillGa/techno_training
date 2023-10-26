from fastapi import FastAPI
from .nba_api_functions import get_games

app = FastAPI()


@app.get("/")
def read_root():
    """Root endpoint returning Hello world object

    Returns:
        dict: Hello key with world value.
    """
    return {"Hello": "World"}


@app.get("/games/{date_param}")
def return_games_from_date(date_param: str):
    """Games endpoint with date filtering on any provided date.

    Args:
        date_param (str): Param date in the following format "yyyy-mm-dd".
                          Used to filter games.

    Returns:
        list[str]: get_games output.
    """
    return get_games(date_param)


@app.get("/games/")
def return_games_todays_date():
    """Games endpoint without date parameter. In that case, use today's date.

    Returns:
        list[str]: get_games output.
    """
    return get_games()
