import csv
import os
from animalcros.models.collectable import Collectable

class Insect(Collectable):
    def __init__(self, name, season, time_of_day, price, weather, location, image_filename):
        super().__init__(name, season, time_of_day, price, image_filename)
        self.weather = weather
        self.location = location

    def get_details(self):
        return {
            "Weather": self.weather,
            "Location": self.location
        }

    @staticmethod
    def _load_data():
        insect_list = []
        path = os.path.join("animalcros", "data", "insects.csv")
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                filename = f"{row['Name'].lower().replace(' ', '_')}.png"
                insect_list.append(Insect(
                    name=row['Name'],
                    season=row.get('Season', ''),
                    time_of_day=row.get('Time', ''),
                    price=row.get('Price', ''),
                    weather=row.get('Weather', ''),
                    location=row.get('Location', ''),
                    image_filename=filename
                ))
        return insect_list