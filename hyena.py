from animal import Animal


class Hyena(Animal):
    def __init__(self, species, name, age, sex, color, weight, origin, birth_date, unique_id):
        super().__init__(species, name, age, sex, color, weight, origin, birth_date, unique_id)
