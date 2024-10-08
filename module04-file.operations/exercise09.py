import csv

countries = [
    ("tur", "turkey", "asia", 80000000.0),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000.0)
]

with open("countries.csv", "wt", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(countries)
