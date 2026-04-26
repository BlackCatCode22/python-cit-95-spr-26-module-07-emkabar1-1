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

print(animal_names)