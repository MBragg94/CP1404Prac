FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def load_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip the header row
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) < 3:  # Skip blank or malformed lines
                continue
            records.append(parts)
    return records


def process_records(records):
    champion_to_count = {}
    countries = set()

    for record in records:
        country = record[INDEX_COUNTRY]
        champion = record[INDEX_CHAMPION]
        countries.add(country)
        # Count wins
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1

    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion}: {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
