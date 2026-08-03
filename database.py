import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = int(os.getenv('DB_PORT'))

def get_connection():
    return psycopg2.connect(
            host = host,
            database = database,
            user = user,
            password = password,
            port = port
    )

def insert_query_series(seriesList):
    query = '''INSERT INTO SERIES(tmdb_id, title, description, genre, language, released_on, rating, popularity, adult, poster)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (tmdb_id) DO NOTHING ;'''
    values = (seriesList['tmdb_id'], seriesList['title'], seriesList['description'], seriesList['genre'], seriesList['language'], seriesList['released_on'], seriesList['rating'], seriesList['popularity'], seriesList['adult'], seriesList['poster'])
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query, values)

def insert_query_movies(moviesList):
    query = '''INSERT INTO MOVIES(tmdb_id, title, description, genre, language, released_on, rating, popularity, adult, poster)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (tmdb_id) DO NOTHING ;'''
    values = (moviesList['tmdb_id'], moviesList['title'], moviesList['description'], moviesList['genre'], moviesList['language'], moviesList['released_on'], moviesList['rating'], moviesList['popularity'], moviesList['adult'], moviesList['poster'])
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query, values)

def search_series(title):
    query = 'SELECT title, rating FROM SERIES WHERE title ILIKE %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (f'%{title}%',))
            return cur.fetchall()

def get_random_series():
    query = '''SELECT tmdb_id, title, description, genre, language, released_on, poster
    FROM SERIES ORDER BY RANDOM() LIMIT 1 ;'''
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchone()

def get_top_rated_series(count):
    query = 'SELECT title, rating FROM SERIES ORDER BY RATING DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (count,))
            return cur.fetchall()

def get_popular_series(count):
    query = 'SELECT title, rating FROM SERIES ORDER BY POPULARITY DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (count,))
            return cur.fetchall()

def get_series_by_genre(genre, count):
    query = 'SELECT title, rating FROM SERIES WHERE genre ILIKE %s ORDER BY RATING DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (f'%{genre}%', count))
            rows = cur.fetchall()
            print(rows)
            return rows

def get_series_by_language(language, count):
    query = 'SELECT title, rating FROM SERIES WHERE language ILIKE %s ORDER BY RATING DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (f'%{language}%', count))
            return cur.fetchall()

def search_movie(title):
    query = 'SELECT title, rating FROM MOVIES WHERE title ILIKE %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (f'%{title}%',))
            return cur.fetchall()

def get_random_movie():
    query = '''SELECT tmdb_id, title, description, genre, language, released_on, rating, poster
    FROM MOVIES ORDER BY RANDOM() LIMIT 1 ;'''
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchone()

def get_top_rated_movies(count):
    query = 'SELECT title, rating FROM MOVIES ORDER BY RATING DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (count,))
            return cur.fetchall()

def get_popular_movies(count):
    query = 'SELECT title, rating FROM MOVIES ORDER BY POPULARITY DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (count,))
            return cur.fetchall()

def get_movies_by_genre(genre, count):
    query = 'SELECT title, rating FROM MOVIES WHERE genre ILIKE %s ORDER BY RATING DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (f'%{genre}%', count))
            return cur.fetchall()

def get_movies_by_language(language, count):
    query = 'SELECT title, rating FROM MOVIES WHERE language ILIKE %s ORDER BY RATING DESC LIMIT %s ;'
    with get_connection() as con:
        with con.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(query, (f'%{language}%', count))
            return cur.fetchall()

def get_total_movies():
    query = 'SELECT COUNT(*) FROM MOVIES ;'
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()[0][0]

def get_total_series():
    query = 'SELECT COUNT(*) FROM SERIES ;'
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()[0][0]

def get_all_genre_movies():
    query = 'SELECT DISTINCT genre FROM MOVIES ORDER BY genre ;'
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query)
            genres = [row[0] for row in cur.fetchall()]
            return genres

def get_all_genre_series():
    query = 'SELECT DISTINCT genre FROM SERIES ORDER BY genre ;'
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query)
            genres = [row[0] for row in cur.fetchall()]
            return genres

def get_all_language_movies():
    query = 'SELECT DISTINCT language FROM MOVIES ORDER BY language ;'
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query)
            language = [row[0] for row in cur.fetchall()]
            return language

def get_all_language_series():
    query = 'SELECT DISTINCT language FROM SERIES ORDER BY language ;'
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query)
            language = [row[0] for row in cur.fetchall()]
            return language

