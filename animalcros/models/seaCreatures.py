import csv
import os
from animalcros.models.collectable import Collectable

class SeaCreature(Collectable):
    def __init__(self, name, season, time_of_day, price, speed, size, image_filename):
        super().__init__(name, season, time_of_day, price, image_filename)
        self.speed = speed
        self.size = size

    def get_details(self):
        return {
            "Speed": self.speed,
            "Size": self.size
        }

    @staticmethod
    def _load_data():
        creature_list = []
        path = os.path.join("animalcros", "data", "seaCreatures.csv")
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                filename = f"{row['Name'].lower().replace(' ', '_')}.png"
                creature_list.append(SeaCreature(
                    name=row['Name'],
                    season=row.get('Season', ''),
                    time_of_day=row.get('Time', ''),
                    price=row.get('Price', ''),
                    speed=row.get('Speed', ''),
                    size=row.get('Size', ''),
                    image_filename=filename
                ))
        return creature_list