import discord
from discord.ext import commands
import logging
import os
import database as db
import discord_embeds as dce
import discord_buttons as dcb
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('BOT_TOKEN')
color = int(os.getenv('COLOR_CODE'), 16)
image = os.getenv('IMAGE_URL')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot=commands.Bot(command_prefix='r!',intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity = discord.Game(name = "🍿 Finding Your Next Watch"))
    print(bot.guilds)
    print(len(bot.guilds))
    print(f'Logging in as {bot.user}')

@bot.tree.command(name = "help", description = "View all available commands")
async def help(interaction: discord.Interaction):
    embed  = dce.embed_help()
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "ping", description = "Check the bot's response time")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency*1000, 2)
    embed = dce.embed_ping(latency)
    view = dcb.Ping(latency)
    await interaction.response.send_message(embed = embed, view = view)

@bot.tree.command(name = "about", description = "Learn more about PLATYPUS")
async def about(interaction: discord.Interaction):
    embed = dce.embed_about()
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "stats", description = "View bot and database statistics")
async def stats(interaction: discord.Interaction):
    latency = round(bot.latency*1000,2)
    totalMovies = db.get_total_movies()
    totalSeries = db.get_total_series()
    embed = dce.embed_stats(latency, totalMovies, totalSeries)
    await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "random-movie", description = "Get a random movie recommendation")
async def random_movie(interaction: discord.Interaction):
    movie = db.get_random_movie()
    print(movie)
    embed = dce.embed_random_movie(movie, interaction.user)
    await interaction.response.send_message(embed = embed)   

@bot.tree.command(name = "random-series", description = "Get a random TV series recommendation")
async def random_series(interaction: discord.Interaction):
    series = db.get_random_series()
    print(series)
    embed = dce.embed_random_series(series, interaction.user)
    await interaction.response.send_message(embed = embed)   

@bot.tree.command(name = "top-rated-movies", description = "Browse the highest rated movies")
async def top_rated_movies(interaction: discord.Interaction, count: int):
    serial = 1
    if count > 50:
        count = 50
    movies = db.get_top_rated_movies(count)
    if count > 25:
        page1 = movies[:25]
        page2 = movies[25:]
        embed = dce.embed_top_rated_movies(page1, 1, 2, interaction.user, count, serial)
        embedFxn = dce.embed_top_rated_movies
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_top_rated_movies(movies, 1, 1, interaction.user, count, serial)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "top-rated-series", description = "Browse the highest rated TV series")
async def top_rated_series(interaction: discord.Interaction, count: int):
    serial = 1
    if count > 50:
        count = 50
    series = db.get_top_rated_series(count)
    if count > 25:
        page1 = series[:25]
        page2 = series[25:]
        embed = dce.embed_top_rated_series(page1, 1, 2, interaction.user, count, serial)
        embedFxn = dce.embed_top_rated_series
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_top_rated_series(series, 1, 1, interaction.user, count, serial)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "popular-movies", description = "Discover the most popular movies")
async def popular_movies(interaction: discord.Interaction, count: int):
    serial = 1
    if count > 50:
        count = 50
    movies = db.get_popular_movies(count)
    if count > 25:
        page1 = movies[:25]
        page2 = movies[25:]
        embed = dce.embed_popular_movies(page1, 1, 2, interaction.user, count, serial)
        embedFxn = dce.embed_popular_movies
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_popular_movies(movies, 1, 1, interaction.user, count, serial)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "popular-series", description = "Discover the most popular TV series")
async def popular_series(interaction: discord.Interaction, count: int):
    serial = 1
    if count > 50:
        count = 50
    series = db.get_popular_series(count)
    if count > 25:
        page1 = series[:25]
        page2 = series[25:]
        embed = dce.embed_popular_series(page1, 1, 2, interaction.user, count, serial)
        embedFxn = dce.embed_popular_series
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_popular_series(series, 1, 1, interaction.user, count, serial)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "movies-language", description = "Find Movies by language")
async def movies_language(interaction: discord.Interaction, count: int, language: str):
    serial = 1
    if count > 50:
        count = 50
    movies = db.get_movies_by_language(language, count)
    if not movies:
        await interaction.response.send_message(f'No movies found for **{language.upper()}**.', ephemeral = True)
        return
    if count > 25:
        page1 = movies[:25]
        page2 = movies[25:]
        embed = dce.embed_movies_by_language(page1, 1, 2, interaction.user, count, serial, language)
        embedFxn = dce.embed_movies_by_language
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, language = language, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_movies_by_language(movies, 1, 1, interaction.user, count, serial, language)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "series-language", description = "Find TV series by language")
async def series_language(interaction: discord.Interaction, count: int, language: str):
    serial = 1
    if count > 50:
        count = 50
    series = db.get_series_by_language(language, count)
    if not series:
        await interaction.response.send_message(f'No series found for **{language.upper()}**.', ephemeral = True)
        return
    if count > 25:
        page1 = series[:25]
        page2 = series[25:]
        embed = dce.embed_series_by_language(page1, 1, 2, interaction.user, count, serial, language)
        embedFxn = dce.embed_series_by_language
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, language = language, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_series_by_language(series, 1, 1, interaction.user, count, serial, language)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "movies-genre", description = "Find Movies by genre")
async def movies_genre(interaction: discord.Interaction, count: int, genre: str):
    serial = 1
    if count > 50:
        count = 50
    movies = db.get_movies_by_genre(genre, count)
    if not movies:
        await interaction.response.send_message(f'No movies found for **{genre.upper()}**.', ephemeral = True)
        return
    if count > 25:
        page1 = movies[:25]
        page2 = movies[25:]
        embed = dce.embed_movies_by_genre(page1, 1, 2, interaction.user, count, serial, genre)
        embedFxn = dce.embed_movies_by_genre
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, genre = genre, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_movies_by_genre(movies, 1, 1, interaction.user, count, serial, genre)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "series-genre", description = "Find TV series by genre")
async def series_genre(interaction: discord.Interaction, count: int, genre: str):
    serial = 1
    if count > 50:
        count = 50
    series = db.get_series_by_genre(genre, count)
    if not series:
        await interaction.response.send_message(f'No series found for **{genre.upper()}**.', ephemeral = True)
        return
    if count > 25:
        page1 = series[:25]
        page2 = series[25:]
        embed = dce.embed_series_by_genre(page1, 1, 2, interaction.user, count, serial, genre)
        embedFxn = dce.embed_series_by_genre
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, genre = genre, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_series_by_genre(series, 1, 1, interaction.user, count, serial, genre)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "search-movies", description = "Search movies by title")
async def search_movies(interaction: discord.Interaction, title: str):
    serial = 1
    movies = db.search_movie(title)
    if not movies:
        await interaction.response.send_message(f'No movies found for **{title.upper()}**.', ephemeral = True)
        return
    if len(movies) > 50:
        movies = movies[:50]
    if len(movies) > 25:
        page1 = movies[:25]
        page2 = movies[25:]
        embed = dce.embed_movies_by_title(page1, 1, 2, interaction.user, serial, title)
        embedFxn = dce.embed_movies_by_title
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, title = title, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_movies_by_title(movies, 1, 1, interaction.user, serial, title)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "search-series", description = "Search TV series by title")
async def search_series(interaction: discord.Interaction, title: str):
    serial = 1
    series = db.search_series(title)
    if not series:
        await interaction.response.send_message(f'No series found for **{title.upper()}**.', ephemeral = True)
        return
    if len(series) > 50:
        series = series[:50]
    if len(series) > 25:
        page1 = series[:25]
        page2 = series[25:]
        embed = dce.embed_series_by_title(page1, 1, 2, interaction.user, serial, title)
        embedFxn = dce.embed_series_by_title
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, title = title, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_series_by_title(series, 1, 1, interaction.user, serial, title)
        await interaction.response.send_message(embed = embed)

@bot.tree.command(name = "genres", description = "View all available genres")
async def genres(interaction: discord.Interaction):
    serial = 1
    genres = db.get_all_genre_movies()
    genreSeries = db.get_all_genre_series()
    for genre in genreSeries:
        if genre not in genres:
            genres.append(genre)
    count = len(genres)
    if len(genres) > 50:
        genres = genres[:25]
    if len(genres) > 25:
        page1 = genres[:25]
        page2 = genres[25:]
        embed = dce.embed_genres(page1, 1, 2, interaction.user, count, serial)
        embedFxn = dce.embed_genres
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_genres(genres, 1, 1, interaction.user, count, serial)
        await interaction.response.send_message(embed = embed)    

@bot.tree.command(name = "languages", description = "View all available languages")
async def languages(interaction: discord.Interaction):
    serial = 1
    languages = db.get_all_language_movies()
    languageSeries = db.get_all_language_series()
    for language in languageSeries:
        if language not in languages:
            languages.append(language)
    count = len(languages)
    if len(languages) > 50:
        languages = languages[:50]
    if len(languages) > 25:
        page1 = languages[:25]
        page2 = languages[25:]
        embed = dce.embed_languages(page1, 1, 2, interaction.user, count, serial)
        embedFxn = dce.embed_languages
        view = dcb.Buttons(page1, page2, embedFxn, interaction.user, count = count, serial = serial + 25)
        await interaction.response.send_message(embed = embed, view = view)
    else:
        embed = dce.embed_languages(languages, 1, 1, interaction.user, count, serial)
        await interaction.response.send_message(embed = embed)    

def run():
    bot.run(token)

def main():
    try:
        run()
    except Exception as error:
        print(error)
        print("Unable to fetch data currently")    

if __name__ == "__main__":
    main()


    