from datetime import date
import requests


def get_games(date_param: str = date.today().strftime("%Y-%m-%d")):
    """This function retrieves the NBA games and returns a string array of the
    provided date

    Args:
        date_param (str, optional): Requested games date, format : 'yyyy-mm-dd'
                                    Defaults to
                                    date.today().strftime("%Y-%m-%d").

    Returns:
        list[str]: String array containing the different NBA games of the day.
                    Each element has the following format :
                    "Visitor City Team @ Home City Team".
    """
    response = requests.get(
        f'https://www.balldontlie.io/api/v1/games?\
        seasons[]=2023&dates[]="{date_param}"'
    )
    games = []

    for item in response.json()["data"]:
        visitors = item["visitor_team"]["full_name"]
        home = item["home_team"]["full_name"]
        game = f"{visitors} @ {home}"
        games.append(game)

    output = {
        "date": date_param,
        "status_code": response.status_code,
        "games": games,
    }
    return output
