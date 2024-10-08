import json

with open("resources/movies.json", "rt") as file:
    movies = json.load(file)
    # histogram -> genre