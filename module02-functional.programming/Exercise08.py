import json
from collections import defaultdict
from functools import reduce


def histogramReducer(histogram, continent):
    if not continent in histogram:
        histogram[continent] = 1
    else:
        histogram[continent] += 1
    return histogram


def histogramReducer2(histogram, continent):
    histogram[continent] = histogram.get(continent, 0) + 1
    return histogram

def histogramReducer3(histogram, continent):
    histogram[continent] += 1
    return histogram


with open("resources/countries.json", mode="rt", encoding="utf-8") as file:
    countries = json.load(file)
    continentCountries = reduce(histogramReducer3, map(lambda country: country["continent"], countries), defaultdict(int))
    print(continentCountries)
