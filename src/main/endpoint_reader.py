import requests
from src.main.constants import MAIN_URL


def get_response(token: str) -> requests.Response:
    return requests.get(MAIN_URL, headers={'Authorization': token})
