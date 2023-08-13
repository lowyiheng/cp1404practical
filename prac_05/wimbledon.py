FILENAME = "wimbledon.txt"


def main():
    datas = read_csv_file(FILENAME)
    champions = calculate_champions(datas)
    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")
    countries = get_countries(datas)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)


def read_csv_file(filename):
    datas = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            datas.append(parts)
    return datas


def calculate_champions(data):
    champions = {}
    for row in data:
        name = row[2]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    sorted_countries = sorted(countries)
    return sorted_countries


main()
