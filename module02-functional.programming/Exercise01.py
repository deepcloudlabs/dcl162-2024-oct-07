countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80000000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67000000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60000000}
]
# total population of european countries
# imperative programming
total_population = 0
for country in countries: # external loop
    if country["continent"] == "europe":
        population = country["population"]
        total_population += population
print(f"total population: {total_population}")

# declarative programming: functional programming
# 1. High-order function: filter, map, reduce, ...
#    method chain: filter -> map -> sum
#         countries -> pipeline(method chain) -> solution
# 2. Pure function: lambda expression
to_population = lambda a_country: a_country["population"]
is_european = lambda a_country: a_country["continent"] == "europe"
total_population = sum(map(to_population, filter(is_european, countries)))
print(f"total population: {total_population}")

