from abc import ABC, abstractmethod

# Requirement 1: Abstract Base Class
class StationAsset(ABC):
    @abstractmethod
    def calculate_revenue(self):
        pass

# Requirement 2: Inheritance (FuelDispenser is a StationAsset)
class FuelDispenser(StationAsset):
    def __init__(self, liters_sold, price_per_liter):
        self.liters_sold = liters_sold
        self.price_per_liter = price_per_liter

    # Requirement 3: Unique logic for Fuel
    def calculate_revenue(self):
        return self.liters_sold * self.price_per_liter

# Requirement 2: Inheritance (CarWash is a StationAsset)
class CarWash(StationAsset):
    def __init__(self, cars_washed, price_per_wash):
        self.cars_washed = cars_washed
        self.price_per_wash = price_per_wash

    # Requirement 3: Unique logic for Car Wash
    def calculate_revenue(self):
        return self.cars_washed * self.price_per_wash
