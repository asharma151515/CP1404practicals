
"""
CP1404/CP5632 Practical
Processing Wimbledon gentlemen's singles champions data
"""



# Read and process the Wimbledon champions data from the wimbledon.csv file
with open('wimbledon.csv', 'r') as file:
    data = [line.strip().split(',') for line in file]

# Create a dictionary to store the champions and their win counts
champions = {}
countries = set()

for entry in data:
    champion = entry[1]
    country = entry[2]

    champions[champion] = champions.get(champion, 0) + 1
    countries.add(country)

# Display the champions and their win counts
print("Wimbledon Champions:")
for champion, wins in champions.items():
    print(f"{champion} {wins}")

# Display the countries of the champions in alphabetical order
country_list = sorted(list(countries))
print("\nThese 12 countries have won Wimbledon:")
print(", ".join(country_list))
