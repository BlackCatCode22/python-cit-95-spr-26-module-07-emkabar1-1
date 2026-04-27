from animal import Animal
from datetime import date


class Bear(Animal):
    def __init__(self, species, name, age, sex, color, weight, origin, birth_date, unique_id):
        super().__init__(species, name, age, sex, color, weight, origin, birth_date, unique_id)

        is_winter = date.today().month in [12, 1, 2]
        self.is_hibernating = is_winter

    def __str__(self):
        status = '(Currently Hibernating)' if self.is_hibernating else ''
        return f'{super().__str__()} {status}'

    def say_catchphrase(self):
        famous_phrases = {
            'Smokey': 'Only you can prevent wildfires.',
            'Winnie the Pooh': 'Oh, bother.',
            'Yogi': "I'm smarter than the average bear!",
            'Baloo': "Look for the bare necessities."
        }
        return famous_phrases.get(self.name)
