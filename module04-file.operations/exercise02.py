with open("countries.txt", "rt") as countries:
    for line in countries:
        try:
            code, name, continent, population = line.strip().split(",")
            print(f"{code},{name},{continent},{population}")
        except ValueError as ve:
            print(f"Cannot parse {line}: {ve}")
