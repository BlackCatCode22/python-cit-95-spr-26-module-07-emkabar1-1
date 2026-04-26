class Animal:
    def __init__(self, species, age, sex, color, weight, origin):
        self.species = species
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
        self.origin = origin

    def get_all_values(self):
        return vars(self)
