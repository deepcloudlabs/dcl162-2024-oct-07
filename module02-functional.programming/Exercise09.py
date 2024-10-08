import json
from functools import reduce
from itertools import chain


def genreHistogramReducer(histogram, genre):
    histogram[genre] = histogram.get(genre, 0) + 1
    return histogram


with open("resources/movies.json", "rt") as file:
    movies = json.load(file)
    # flattening: chain.from_iterable
    movieGenreHistogram = reduce(genreHistogramReducer, chain.from_iterable(filter(lambda genres: len(genres) > 0,
                                                                                   map(lambda movie: [genre["name"] for
                                                                                                      genre in
                                                                                                      movie["genres"]],
                                                                                       movies))), {})
    print(movieGenreHistogram)
