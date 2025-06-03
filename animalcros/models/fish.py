import csv
import os
from animalcros.models.collectable import Collectable

class Fish(Collectable):
    def __init__(self, name, season, time_of_day, price, location, size, image_filename):
        super().__init__(name, season, time_of_day, price, image_filename)
        self.location = location
        self.size = size

    def get_details(self):
        return {
            "Location": self.location,
            "Size": self.size
        }

    @staticmethod
    def _load_data():
        fish_list = []
        path = os.path.join("animalcros", "data", "fish.csv")
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                filename = f"{row['Name'].lower().replace(' ', '_')}.png"
                fish_list.append(Fish(
                    name=row['Name'],
                    season=row.get('Season', ''),
                    time_of_day=row.get('Time', ''),
                    price=row.get('Price', ''),
                    location=row.get('Location', ''),
                    size=row.get('Size', ''),
                    image_filename=filename
                ))
        return fish_list