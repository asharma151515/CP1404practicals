class Taxi:
    price_per_km = 1.23  # base price per km

    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.current_fare_distance = 0
        self.odometer = 0

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
        self.current_fare_distance += distance
        self.fuel -= distance
        self.odometer += distance
        return distance

    def get_fare(self):
        return round(self.price_per_km * self.current_fare_distance, 2)

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        return self.flagfall + super().get_fare()

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"
