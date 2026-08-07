import time
import requests
import os
from dotenv import load_dotenv
load_dotenv()

baseUrl = os.getenv('BASE_URL')
endpointSeries = os.getenv('ENDPOINT_GENRE_SERIES')
endpointMovies = os.getenv('ENDPOINT_GENRE_MOVIES')
endpointLanguage = os.getenv('ENDPOINT_LANGUAGE')
auth = os.getenv('API_ACCESS_TOKEN')

genreSeries = {}
genreMovies = {}
language = {}

headers = {
    "accept": "application/json",
    "Authorization": f'Bearer {auth}'
}

def fetch_genre(baseUrl, endpoint, headers, genreSet):
  for attempt in range(5):
    try:
      r = requests.get(baseUrl + endpoint, headers = headers, timeout = 10)
      r.raise_for_status()
      response = r.json()["genres"]
      return create_genre_map(response, genreSet)

    except requests.exceptions.RequestException as e:
      print(e)
      time.sleep(3)

  raise Exception("Couldn't fetch genre map")

def fetch_language(baseUrl, endpoint, headers, langSet):
  for attempt in range(5):
    try:
      r = requests.get(baseUrl + endpoint, headers = headers, timeout = 10)
      r.raise_for_status()
      response = r.json()
      return create_language_map(response, langSet)

    except requests.exceptions.RequestException as e:
      print(e)
      time.sleep(3)

  raise Exception("Couldn't fetch language map")

def create_genre_map(response, genreSet):
  for data in response:
    genreSet[data['id']] = data['name']
  return genreSet  

def create_language_map(response, langSet):
  for data in response:
    langSet[data['iso_639_1']] = data['english_name']
  return langSet

def load_tmdb():
    try:

        print("Fetching series genres...")
        fetch_genre(baseUrl, endpointSeries, headers, genreSeries)

        print("Fetching movie genres...")
        fetch_genre(baseUrl, endpointMovies, headers, genreMovies)

        print("Fetching languages...")
        fetch_language(baseUrl, endpointLanguage, headers, language)

        print(genreMovies)
        print(language)

        return genreSeries, genreMovies, language

    except Exception as error:
        print("ERROR:", error)
        return {}, {}, {}

if __name__ == "__main__":
  load_tmdb()