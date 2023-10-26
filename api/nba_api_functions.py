from datetime import date
import requests

def get_games(date_param: str = date.today().strftime("%Y-%m-%d")):
    response = requests.get(f"https://www.balldontlie.io/api/v1/games?seasons[]=2023&dates[]=\"{date_param}\"")
    games = []

    for item in response.json()["data"]:
        visitors = item["visitor_team"]["full_name"]
        home = item["home_team"]["full_name"]
        game = f"{visitors} @ {home}"
        games.append(game)

    output = {
        "date": date_param,
        "status_code": response.status_code,
        "games": games
    }
    return output