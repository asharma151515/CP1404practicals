### taxi.py


class Car:
    """Represent a car object."""

    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        """Drive the car a given distance."""
        self.odometer += distance
        return distance

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}"


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23  # Class variable for price per kilometer

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.current_fare_distance = 0  # Distance driven for the current fare

    def drive(self, distance):
        """Drive the taxi a given distance and calculate fare."""
        if distance > self.fuel:
            distance = self.fuel  # Can't drive more than available fuel
        self.fuel -= distance
        self.current_fare_distance += distance
        self.odometer += distance
        return distance

    def get_fare(self):
        """Calculate the fare based on the distance driven."""
        return self.current_fare_distance * self.price_per_km

    def start_fare(self):
        """Reset the fare distance for a new fare."""
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation of the taxi."""
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km}/km"


# Example usage (not part of the taxi.py file)
if __name__ == "__main__":
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
