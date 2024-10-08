countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80000000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67000000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60000000}
]


def to_population(a_country):
    print(f"to_population({a_country["name"]})")
    return a_country["population"]


def is_european(a_country):
    print(f"is_european({a_country["name"]})")
    return a_country["continent"] == "europe"


total_population = sum(map(to_population, filter(is_european, countries)))
print(f"total population: {total_population}")
