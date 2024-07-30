"""
CP1404/CP5632 Practical
Taxi Test
"""

from taxi import Taxi  # Import the Taxi class from taxi.py


def main():
    # Create a new taxi object
    my_taxi = Taxi("Prius 1", 100)  # Name: "Prius 1", Fuel: 100 units

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)  # This will use the __str__ method
    print(f"Current fare: ${my_taxi.get_fare():.2f}")  # Print the fare

    # Restart the meter (start a new fare) and then drive the car 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print the details and the current fare again
    print(my_taxi)  # This will use the __str__ method
    print(f"Current fare: ${my_taxi.get_fare():.2f}")  # Print the fare


if __name__ == "__main__":
    main()
