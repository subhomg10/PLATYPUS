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

baseUrl = os.getenv('BASE_URL')
endpoint = os.getenv('ENDPOINT_SERIES')
auth = os.getenv('API_ACCESS_TOKEN')

seriesSet = []
seriesId = []
failedPages = []

headers = {
    "accept": "application/json",
    "Authorization": f'Bearer {auth}'
}

def fetch_series(baseUrl, endpoint, page, headers, seriesSet):
    for attempt in range(5):
        try:
            r = requests.get(
                baseUrl + endpoint + f"{page}",
                headers=headers,
                timeout=10
            )
            r.raise_for_status()
            response = r.json()["results"]
            return clean_series(response, seriesSet)

        except requests.exceptions.RequestException as e:
            print(f"Page {page} failed (attempt {attempt+1}): {e}")
            time.sleep(3)

    print(f"Skipping page {page}")
    failedPages.append(page)
    print(failedPages)

def clean_series(response, seriesSet):
    for series in response:
        if series['original_language'] == "ja":
            continue
        seriesList = {
            'tmdb_id' : series['id'],
            'title' : series['name'],
            'description' : series.get('overview') or "No description available",
            'genre' : get_genre(series.get('genre_ids', [])),
            'language' : get_language(series.get('original_language')),
            'released_on' : series.get('first_air_date') or None,
            'rating' : series.get('vote_average') or None,
            'popularity' : series.get('popularity') or None,
            'adult' : series.get('adult', False),           
            'poster' : series.get('poster_path') or None
        }
        get_series(seriesList, seriesSet)
    return seriesSet

def get_series(seriesList, seriesSet):
    if len(seriesSet) < 1000:
        if seriesList['tmdb_id'] not in seriesId:
            seriesSet.append(seriesList)
            seriesId.append(seriesList['tmdb_id'])
            insert_series(seriesList)
    return seriesSet

def insert_series(seriesList):
    db.insert_query_series(seriesList)

def get_genre(genreIds):
    genreSet = []
    for id in genreIds:
        if id in genreSeries:
            genreSet.append(genreSeries[id])
    if len(genreSet) == 0:
        return "Unknown"
    return ", ".join(genreSet)

def get_language(langCode):
    if langCode in language:
        return language[langCode]
    return "Language Unavailable"
    

def series():
    for i in range(1, 143):
        if len(seriesSet) >= 1000:
            break
        fetch_series(baseUrl, endpoint, i, headers, seriesSet)

def main():
    try:
        series()
    except requests.exceptions.RequestException as error:
        print(f'Connection Failed {error}')

if __name__ == "__main__":
    main()
