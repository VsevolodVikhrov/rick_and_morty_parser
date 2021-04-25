import requests
url = 'https://rickandmortyapi.com/api/character/'


def get_characters():
    return requests.get(url).json()['results']
