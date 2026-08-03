import discord
import os
from dotenv import load_dotenv
load_dotenv()

color = int(os.getenv('COLOR_CODE'), 16)
thumbnail = os.getenv('PLATYPUS_THUMBNAIL')
image = os.getenv('PLATYPUS_IMAGE')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

def embed_top_rated_movies(moviesArray, pageNo, totalPages, user, count, serial):
    embed = discord.Embed(
        title = f'⭐  Top {count} Rated Movies',
        description = "Here are the top-rated Movies available.",
        color = color
    )
    for movie in moviesArray:
        title = movie['title']
        rating = round(movie['rating'], 1)
    
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial +=  1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_top_rated_series(seriesArray, pageNo, totalPages, user, count, serial):
    embed = discord.Embed(
        title = f'⭐  Top {count} Rated TV Series',
        description = "Here are the top-rated TV Series available.",
        color = color
    )
    for series in seriesArray:
        title = series['title']
        rating = round(series['rating'], 1)

        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_popular_movies(moviesArray, pageNo, totalPages, user, count, serial):
    embed = discord.Embed(
        title = f'⭐  Top {count} Popular Movies',
        description = "Here are the most popular Movies available.",
        color = color
    )
    for movie in moviesArray:
        title = movie['title']
        rating = movie['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)
            
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_popular_series(seriesArray, pageNo, totalPages, user, count, serial):
    embed = discord.Embed(
        title = f'⭐  Top {count} Popular Movies',
        description = "Here are the most popular TV Series available.",
        color = color
    )
    for series in seriesArray:
        title = series['title']
        rating = series['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)
            
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_movies_by_language(moviesArray, pageNo, totalPages, user, count, serial, language):
    embed = discord.Embed(
        title = f'⭐  Top {count} {language.upper()} Movies',
        description = f'Here are the top-rated **{language.upper()}** Movies available.',
        color = color
    )
    for movie in moviesArray:
        title = movie['title']
        rating = movie['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)
            
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_series_by_language(seriesArray, pageNo, totalPages, user, count, serial, language):
    embed = discord.Embed(
        title = f'⭐  Top {count} {language.upper()} TV Series',
        description = f'Here are the top-rated **{language.upper()}** TV Series available.',
        color = color
    )
    for series in seriesArray:
        title = series['title']
        rating = series['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)

        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_movies_by_genre(moviesArray, pageNo, totalPages, user, count, serial, genre):
    embed = discord.Embed(
        title = f'⭐  Top {count} {genre.upper()} Movies',
        description = f'Here are the top-rated **{genre.upper()}** Movies available.',
        color = color
    )
    for movie in moviesArray:
        title = movie['title']
        rating = movie['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)
            
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_series_by_genre(seriesArray, pageNo, totalPages, user, count, serial, genre):
    embed = discord.Embed(
        title = f'⭐  Top {count} {genre.upper()} Movies',
        description = f'Here are the top-rated **{genre.upper()}** TV Series available.',
        color = color
    )
    for series in seriesArray:
        title = series['title']
        rating = series['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)
            
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_movies_by_title(moviesArray, pageNo, totalPages, user, serial, title):
    embed = discord.Embed(
        title = f'Showing Results for {title.upper()}',
        description = f'Here are the results found for **{title.upper()}**.',
        color = color
    )
    for movie in moviesArray:
        title = movie['title']
        rating = movie['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)
            
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_series_by_title(seriesArray, pageNo, totalPages, user, serial, title):
    embed = discord.Embed(
        title = f'Showing Results for {title.upper()}',
        description = f'Here are the results found for **{title.upper()}**.',
        color = color
    )
    for series in seriesArray:
        title = series['title']
        rating = series['rating']

        if rating is None:
            rating = "N/A"
        else:
            rating = round(rating, 1)
            
        embed.add_field(
            name = f'{serial}. {title}',
            value = f'Rating:  {rating}',
            inline = False
        )
        serial += 1

    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_random_movie(movie, user):
    tmdbId = movie['tmdb_id']
    title = movie['title']
    description = movie['description']
    genre = movie['genre']
    language = movie['language']
    releasedOn = movie['released_on']
    rating = movie['rating']
    poster = movie['poster']

    if rating is None:
        rating = "N/A"
    else:
        rating = round(rating, 1)
            
    embed = discord.Embed(
        title = f'{title.upper()}',
        description = description,
        color = color
    )
    embed.add_field(
        name = "Additional Information:",
        value = f'**TMDB Id:** {tmdbId}\n**Genre:** {genre}\n**Language:** {language}\n**Released On:** {releasedOn}\n**Rating**: {rating}',
        inline = False
    )
    poster_url = f'https://image.tmdb.org/t/p/w500{poster}'
    embed.set_thumbnail(url = thumbnail)
    if poster:
        embed.set_image(url = poster_url)
    embed.set_footer(text = f'Page 1/1 • Requested by {user.name}')
    return embed

def embed_random_series(series, user):
    tmdbId = series['tmdb_id']
    title = series['title']
    description = series['description']
    genre = series['genre']
    language = series['language']
    releasedOn = series['released_on']
    rating = series['rating']
    poster = series['poster']

    if rating is None:
        rating = "N/A"
    else:
        rating = round(rating, 1)
            
    embed = discord.Embed(
        title = f'{title.upper()}',
        description = description,
        color = color
    )
    embed.add_field(
        name = "Additional Information:",
        value = f'**TMDB Id:** {tmdbId}\n**Genre:** {genre}\n**Language:** {language}\n**First Aired On:** {releasedOn}\n**Rating:** {rating}',
        inline = False
    )
    embed.set_thumbnail(url = thumbnail)
    poster_url = f'https://image.tmdb.org/t/p/w500{poster}'
    if poster:
        embed.set_image(url = poster_url)
    embed.set_footer(text = f'Page 1/1 • Requested by {user.name}')
    return embed

def embed_help():
    embed = discord.Embed(
        title = "🎬  ALL COMMANDS",
        description = "Explore movies, series, and utility commands using the options below.\nUse `/<command-name>`",
        color = color
    )
    embed.add_field(
        name = "**🎥  MOVIES**", 
        value = "• /search-movies\n• /random-movie\n• /top-rated-movies\n• /popular-movies\n• /movie-genre\n• /movie-language", 
        inline = True
    )
    embed.add_field(
        name = "**📺  SERIES**", 
        value = "• /search-series\n• /random-series\n• /top-rated-series\n• /popular-series\n• /series-genre\n• /series-language", 
        inline = True
    )
    embed.add_field(
        name = "**⚙️  UTILITIES**", 
        value = "• /help\n• /about\n• /stats\n• /ping\n• /genres\n• /languages", 
        inline = True
    )
    embed.set_footer(text = "🍿  Happy watching! Hope you find something amazing to watch.")
    embed.set_thumbnail(url = thumbnail)
    return embed

def embed_about():
    embed = discord.Embed(
        title = "🎬  PLATYPUS : Movie & Series Recommendation Bot",
        description = ("PLATYPUS is a Discord bot designed to help users discover movies and TV series through simple slash commands."),
        color = color
    )
    embed.add_field(
        name = "✨  Features",
        value = ("• Search movies and series by name\n• Get random recommendations\n• Explore top-rated and popular content\n• Filter recommendations by genre and language"),
        inline = False
    )
    embed.add_field(
        name = "⚙️  Powered By",
        value=("• Python\n• Discord.py\n• PostgreSQL\n• TMDB API"),
        inline = False
    )
    embed.set_thumbnail(url = thumbnail)
    embed.set_image(url = image)
    embed.set_footer(text = "🍿  Use /help to explore available commands.")
    return embed

def embed_stats(latency, totalMovies, totalSeries):
    embed = discord.Embed(
        title = "📊  PLATYPUS Bot Statistics",
        description = "Here are the current statistics and system information of PLATYPUS.",
        color = color
    )
    embed.add_field(
        name = "🤖  **Bot Information**",
        value = f'• Bot Name: PLATYPUS\n• Status: 🟢  Online\n• Latency: {latency} ms\n• Discord.py Version: 2.5.2',
        inline = False
    )
    embed.add_field(
        name = "🎬  **Database Statistics**",
        value = f'• Total Movies: {totalMovies}\n• Total Series: {totalSeries}\n• Database: PostgreSQL\n• Storage: Local Database Cache',
        inline = False
    )
    embed.add_field(
        name = "⚙️  **System Information**",
        value = "• Language: Python\n• API: TMDB API\n• Hosting: Local",
        inline = False
    )
    embed.set_thumbnail(url = thumbnail)
    embed.set_image(url = image)
    embed.set_footer(text = "🍿  PLATYPUS • Your Personal Movie & Series Assistant")
    return embed

def embed_ping(latency):
    embed = discord.Embed(
        title = "🏓  PONG!",
        description = f"• Latency: `{latency} ms`\n• Status: 🟢  Online",
        color = color
    )
    embed.set_footer(text = "🍿  PLATYPUS • Movie & Series Assistant")
    return embed

def embed_genres(genreArray, pageNo, totalPages, user, count, serial):
    embed = discord.Embed(
        title = "🎭  AVAILABLE GENRES",
        description = f'Explore movies and series by selecting your preferred genre.\nTotal Genres: {count}',
        color = color
    )
    for genre in genreArray:
        embed.add_field(
            name = f'{serial}. {genre}', 
            value = "\u200b",
            inline = False
        )
        serial += 1
    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed

def embed_languages(languageArray, pageNo, totalPages, user, count, serial):
    embed = discord.Embed(
        title = "🎭  AVAILABLE LANGUAGES",
        description = f'Explore movies and series by selecting your preferred language.\nTotal Languages: {count}',
        color = color
    )
    for language in languageArray:
        embed.add_field(
            name = f'{serial}. {language}',
            value = "\u200b",
            inline = False
        )
        serial += 1
    embed.set_footer(text = f'Page {pageNo}/{totalPages} • Requested by {user.name}')
    return embed