import pickle

with open("countries.pkl", "rb") as file:
    countries = pickle.load(file)
    for country in countries:
        print(country)
