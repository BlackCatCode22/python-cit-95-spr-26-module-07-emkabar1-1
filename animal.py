class Animal:
    def __init__(self, species, name, age, sex, color, weight, origin, birth_date, unique_id):
        self.species = species
        self.name = name
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
        self.origin = origin
        self.birth_date = birth_date
        self.animal_id = unique_id

    def __str__(self):
        return f"[{self.animal_id}] {self.name} the {self.species} from {self.origin}"

    def get_all_values(self):
        return vars(self)

    def say_catchphrase(self):
        return None
