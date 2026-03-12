# Requirement 4: Import your classes from the models.py file
from models import FuelDispenser, CarWash

def run_station():
    # Create a list of different assets (Polymorphism)
    assets = [
        FuelDispenser(liters_sold=500, price_per_liter=1.5),
        CarWash(cars_washed=20, price_per_wash=15),
        FuelDispenser(liters_sold=300, price_per_liter=1.6)
    ]

    total_revenue = 0
    
    # Loop through the list and calculate total
    for asset in assets:
        total_revenue += asset.calculate_revenue()

    print(f"Total Station Revenue: ${total_revenue:.2f}")

if __name__ == "__main__":
    run_station()
