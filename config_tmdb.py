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
  r = requests.get(baseUrl + endpoint, headers=headers)
  r.raise_for_status()
  response = r.json()['genres']
  return create_genre_map(response, genreSet)

def fetch_lang(baseUrl, endpoint, headers, langSet):
  r = requests.get(baseUrl + endpoint, headers = headers)
  r.raise_for_status()
  response = r.json()
  return create_langMap(response, langSet)

def create_genre_map(response, genreSet):
  for data in response:
    genreSet[data['id']] = data['name']
  return genreSet  

def create_langMap(response, langSet):
  for data in response:
    langSet[data['iso_639_1']] = data['english_name']
  return langSet

def load_tmdb():
  try:

    fetch_genre(baseUrl, endpointSeries, headers, genreSeries)
    fetch_genre(baseUrl, endpointMovies, headers, genreMovies)
    fetch_lang(baseUrl, endpointLanguage, headers, language)

    return genreSeries, genreMovies, language

  except Exception as error:
    print(error)
    return {},{},{}

if __name__ == "__main__":
  load_tmdb()