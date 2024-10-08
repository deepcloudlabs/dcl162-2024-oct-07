import json


def is_drama(movie):
    for genre in movie['genres']:
        if genre['name'] == 'Drama':
            return True
    return False


def is_drama2(movie):
    return any(genre["name"] == "Drama" for genre in movie["genres"])


_70s = lambda movie: movie["year"] >= 1970 and movie["year"] < 1980

with open("resources/movies.json", "rt") as file:
    movies = json.load(file)
    dramMoviesOf70s = list(filter(is_drama2, filter(_70s, movies)))
    dramMoviesOf70s.sort(key=lambda movie: movie["year"])
    for movie in dramMoviesOf70s:
        print(f"{movie['title']}\t{list(map(lambda genre: genre['name'], movie['genres']))}\t{movie['year']}")
