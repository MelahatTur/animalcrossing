from abc import ABC, abstractmethod

class Collectable(ABC):
    def __init__(self, name, season, time_of_day, price, image_filename):
        self.name = name
        self.season = season
        self.time_of_day = time_of_day
        self.price = price
        self.image_filename = image_filename

    @abstractmethod
    def get_details(self):
        """Return a dictionary of the collectable-specific fields"""
        pass