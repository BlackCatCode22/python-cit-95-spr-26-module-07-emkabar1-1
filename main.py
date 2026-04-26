from animal import Animal

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
        age = first_part[0]
        sex = first_part[3]
        species = first_part[4].capitalize()

        # Season (Keeps "unknown" or "spring"/"fall"/"winter")
        season = parts[1].replace('born in ', '')

        # Color (Handles colors containing "and")
        color = parts[2].replace(' color', '')

        weight = parts[3].split()[0]

        # Origin (Joins everything from index 4 to the end)
        # Remove "from " only from the very beginning of the origin string
        origin = ', '.join(parts[4:]).replace('from ', '')

        # Create animal object
        new_animal = Animal(species, age, sex, color, weight, origin)

        arriving_animals.append(new_animal)

for animal in arriving_animals:
    print(animal.get_all_values())
