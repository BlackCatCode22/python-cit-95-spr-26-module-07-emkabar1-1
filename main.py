from animal import Animal
import random
from datetime import date

CURRENT_DATE = date.today()


def gen_birth_date(age, season):
    birth_year = CURRENT_DATE.year - int(age)

    # Define month/day based on season
    dates = {
        'spring': '03-21',
        'summer': '06-21',
        'fall': '09-21',
        'winter': '12-21'
    }
    # Assign date, fallback to Jan 01 if season is "unknown"
    md = dates.get(season, '01-01')
    return f'{birth_year}-{md}'


def gen_unique_id(species, counts):
    # Get first two letters of species and add id number
    prefix = species[:2]
    counts[species] = counts.get(species, 0) + 1
    return f'{prefix}{counts[species]:02d}'


animal_names = {}
current_species = None

with open('animalNames.txt', 'r') as f:
    for line in f:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Identify species name
        if line.endswith('Names:'):
            # Extract the species name
            current_species = line.split()[0]

        # Otherwise, it's a list of names for the current group
        elif current_species:
            # Split by comma & clean up whitespace around each name
            names_list = [name.strip() for name in line.split(',')]
            # Assign the list to current species key
            animal_names[current_species] = names_list

arriving_animals = []

# Initialize counters for each species
species_counter = {k: 0 for k in animal_names.keys()}

with open('arrivingAnimals.txt', 'r') as f:
    for line in f:
        line = line.strip()

        # Split the line into a list by the comma
        parts = [p.strip() for p in line.split(',')]

        # Extract specific indices based on the source structure
        # Index 0: "4 year old female hyena"
        # Index 1: "born in spring"
        # Index 2: "tan color"
        # Index 3: "70 pounds"
        # Index 4: "from Friguia Park"
        # Index 5: "Tunisia"

        # First Part (Age, Sex, Species)
        first_part = parts[0].split()
        age_val = first_part[0]
        sex = first_part[3]
        species_val = first_part[4].capitalize()

        # Season (Keeps "unknown" or "spring"/"fall"/"winter")
        season_val = parts[1].replace('born in ', '')

        # Color (Handles colors containing "and")
        color = parts[2].replace(' color', '')

        weight = parts[3].split()[0]

        # Origin (Joins everything from index 4 to the end)
        # Remove "from " only from the very beginning of the origin string
        origin = ', '.join(parts[4:]).replace('from ', '')

        # Get the list of names for this species
        available_names = animal_names.get(species_val, [])

        if available_names:
            # Assigns a random name from the list
            assigned_name = available_names.pop(random.randrange(len(available_names)))
        else:
            assigned_name = 'Unknown'

        b_day = gen_birth_date(age_val, season_val)

        # Use species counter for id number
        unique_id = gen_unique_id(species_val, species_counter)

        # Create animal object
        new_animal = Animal(species_val, assigned_name, age_val, sex, color, weight, origin, b_day, unique_id)

        arriving_animals.append(new_animal)

for animal in arriving_animals:
    print(animal.get_all_values())
