import time
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import urllib3
urllib3.disable_warnings()
import database as db
from config_tmdb import load_tmdb
genreSeries, genreMovies, language = load_tmdb()

print(len(genreMovies))
print(len(genreSeries))
print(len(language))

print(list(genreMovies.items())[:5])
print(list(language.items())[:5])

baseUrl = os.getenv('BASE_URL')
endpointTopRated = os.getenv('ENDPOINT_MOVIES_TOP_RATED')
endpointPopular = os.getenv('ENDPOINT_MOVIES_POPULAR')
auth = os.getenv('API_ACCESS_TOKEN')

topRatedSet = []
popularSet = []
moviesId = []
failedPages = []

headers = {
    "accept": "application/json",
    "Authorization": f'Bearer {auth}'
}

def fetch_movies(baseUrl, endpoint, page, headers, moviesSet):
    for attempt in range(5):
        try:
            r = requests.get(baseUrl + endpoint + f"{page}", headers = headers, timeout = 10)
            r.raise_for_status()
            response = r.json()["results"]
            return clean_movies(response, moviesSet)

        except requests.exceptions.RequestException as e:
            print(f"Page {page} failed (attempt {attempt+1}): {e}")
            time.sleep(3)

    print(f"Skipping page {page}")
    failedPages.append(page)
    print(failedPages)

def clean_movies(response, moviesSet):
    for movies in response:
        if movies['original_language'] == "ja":
            continue
        moviesList = {
            'tmdb_id' : movies['id'],
            'title' : movies['title'],
            'description' : movies.get('overview'),
            'genre' : get_genre(movies.get('genre_ids', [])),
            'language' : get_language(movies.get('original_language')),
            'released_on' : movies.get('release_date'),
            'rating' : movies.get('vote_average'),
            'popularity' : movies.get('popularity'),
            'adult' : movies.get('adult', False),           
            'poster' : movies.get('poster_path')
        }
        print(movies["genre_ids"])
        print(get_genre(movies["genre_ids"]))

        print(movies["original_language"])
        print(get_language(movies["original_language"]))
        
        get_movies(moviesList, moviesSet)
    return moviesSet

def get_movies(moviesList, moviesSet):
    if len(moviesSet) < 500:
        if moviesList['tmdb_id'] not in moviesId:
            moviesSet.append(moviesList)
            moviesId.append(moviesList['tmdb_id'])
            insert_movies(moviesList)
    return moviesSet

def insert_movies(moviesList):
    db.insert_query_movies(moviesList)

def get_genre(genreIds):
    genreSet = []
    for id in genreIds:
        if id in genreMovies:
            genreSet.append(genreMovies[id])
    if len(genreSet) == 0:
        return "Unknown"
    return ", ".join(genreSet)

def get_language(langCode):
    if langCode in language:
        return language[langCode]
    return "Unavailable"

def top_rated_movies():
    for i in range(1, 150):
        if len(topRatedSet) >= 500:
            break
        fetch_movies(baseUrl, endpointTopRated, i, headers, topRatedSet)

def popular_movies():
    for i in range(1, 150):
        if len(popularSet) >= 500:
            break
        fetch_movies(baseUrl, endpointPopular, i, headers, popularSet)

def main():
    try:
        top_rated_movies()
        popular_movies()
    except requests.exceptions.RequestException as error:
        print(f'Connection Failed {error}')

if __name__ == "__main__":
    main()

