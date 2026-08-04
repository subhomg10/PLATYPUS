# **🎬  PLATYPUS**
A Discord bot that helps users discover movies and TV series through an interactive, database-backed recommendation system powered by Python, PostgreSQL, and the TMDB API.

---

## **✨  Overview**
PLATYPUS is a Discord bot built to make discovering movies and TV series simple and interactive without leaving Discord.

Instead of scrolling endlessly through streaming platforms, users can search, browse, and receive recommendations directly through slash commands.

The bot fetches metadata from TMDB, processes the data, stores it in a PostgreSQL database, and serves recommendations through Discord using embeds, buttons, and pagination.

---

## **🚀  Features**
### 🎥  Movies
- Search movies by title
- Get a random movie recommendation
- Browse top-rated movies
- Browse popular movies
- Discover movies by genre
- Discover movies by language

### **📺  TV Series**
- Search TV series by title
- Get a random TV series recommendation
- Browse top-rated series
- Browse popular series
- Discover series by genre
- Discover series by language

### **📚  Utilities**
- View all available genres
- View all supported languages
- Bot statistics
- About command
- Help command
- Ping command

---

## **⚡  Highlights**
- Modern Slash Commands
- Interactive Discord Buttons
- Multi-page Pagination
- PostgreSQL Database Integration
- REST API Integration (TMDB)
- Automatic Duplicate Prevention
- Environment Variable Configuration
- Retry Logic for API Requests
- Clean Modular Code Structure

---

## **🛠  Tech Stack**
### **Programming Language**

- Python

### **Libraries & Frameworks**

- discord.py
- requests
- urllib3
- psycopg2-binary
- python-dotenv

### **Database**

- PostgreSQL

### **External API**

- TMDB (The Movie Database)

---

## **⚙️  Installation**
1. **Clone the repository**
    `git clone https://github.com/subhomg10/PLATYPUS.git cd PLATYPUS`
2. **Install the required dependencies**
    `pip install -r requirements.txt`
3. **Configure environment variables**
    Create a `.env` file by copying the values from `.env.example` and replace the placeholders with your own credentials.
4. **Set up PostgreSQL**
    Create a PostgreSQL database and update the database credentials in your `.env` file.
5. **Run the bot**
    `python bot.py`

---

## **📁  Project Structure**
- Platypus/
    - screenshots/
    - .env.example
    - .gitignore
    - api_movies.py
    - api_series.py
    - bot.py
    - config_api.py
    - database.py
    - discord_buttons.py
    - discord_embeds.py
    - README.md
    - requirements.txt

---

## **📊  How It Works**
1. Movie and TV metadata is fetched from TMDB.
2. The data is cleaned and transformed.
3. Processed records are stored inside PostgreSQL.
4. Discord slash commands query the database.
5. Results are displayed using rich embeds and interactive buttons.

---

## **🎯  Example Commands**
- `/search-movies`
- `/search-series`

- `/random-movie`
- `/random-series`

- `/top-rated-movies`
- `/top-rated-series`

- `/popular-movies`
- `/popular-series`

- `/movies-genre`
- `/movies-language`

- `/series-genre`
- `/series-language`

- `/genres`
- `/languages`

- `/help`
- `/about`
- `/stats`
- `/ping`

---

## **📌  Future Improvements**
- User watchlists
- Favorite movies & series
- Recommendation history
- Advanced search filters
- Streaming platform information
- Personalized recommendations
- Multi-language interface

## **📸  Bot Preview**
###  **/about**

>Displays an overview of the bot, its purpose, and supported features.

![about](/screenshots/about.png)

### **/help**

>Lists all available slash commands grouped by category for quick navigation.

![help](/screenshots/help.png)

### **/random-movie**

>Returns a randomly selected movie with detailed information including poster, genre, language, release date, and rating(if available).

![random-movie](/screenshots/random_movie.png)

### **/movies-genre**

>Displays movies filtered by a selected genre with a user-defined result count.

![movies-genre](/screenshots/movies_genre.png)

### **/top-rated-movies**

>Browse the highest-rated movies available in the database using interactive button-based pagination.

![top-rated-movies-1](/screenshots/tr_movies1.png)

![top-rated-movies-2](/screenshots/tr_movies2.png)

---

## **🤝  Contributing**
Suggestions, improvements, and pull requests are always welcome.
If you find a bug or have an idea for a new feature, feel free to open an issue.

---

## **📄  License**
This bot is intended as a portfolio project.
It is not continuously hosted, but can be run locally after configuring the required environment variables.

---

## **👨‍💻  Author**
**Subhom Ghosh**

Backend Developer (Python • PostgreSQL • Discord.py)

- GitHub: [View Profile](https://github.com/subhomg10)

- LinkedIn: [View Profile](https://linkedin.com/in/subhomghosh)

Discord Bot: **PLATYPUS**