from animal import Animal


class Lion(Animal):
    def __init__(self, species, name, age, sex, color, weight, origin, birth_date, unique_id):
        super().__init__(species, name, age, sex, color, weight, origin, birth_date, unique_id)
        self.is_pride_leader = (self.name == 'Mufasa')

    def __str__(self):
        status = '(pride leader)' if self.is_pride_leader else ''
        return f'{super().__str__()} {status}'

    def say_catchphrase(self):
        famous_phrases = {
            'Simba': "I just can't wait to be king!",
            'Mufasa': 'Everything the light touches is our kingdom.'
        }
        return famous_phrases.get(self.name)
