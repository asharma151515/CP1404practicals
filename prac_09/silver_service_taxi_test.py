import unittest
from silver_service_taxi import SilverServiceTaxi


class TestSilverServiceTaxi(unittest.TestCase):
    def setUp(self):
        """Create a SilverServiceTaxi instance for testing."""
        self.taxi = SilverServiceTaxi("Silver Limo", 200, 2)  # Fanciness of 2

    def test_initialization(self):
        """Test the initialization of the SilverServiceTaxi."""
        self.assertEqual(self.taxi.name, "Silver Limo")
        self.assertEqual(self.taxi.fuel, 200)
        self.assertEqual(self.taxi.fanciness, 2)
        self.assertEqual(self.taxi.price_per_km, 2.46)  # Assuming Taxi.price_per_km is 1.23

    def test_get_fare_no_distance(self):
        """Test the fare calculation with no distance driven."""
        self.taxi.start_fare()  # Start a new fare
        self.assertEqual(self.taxi.get_fare(), 4.50)  # Only flagfall should apply

    def test_get_fare_with_distance(self):
        """Test the fare calculation with distance driven."""
        self.taxi.start_fare()  # Start a new fare
        self.taxi.drive(10)  # Drive 10 km
        expected_fare = 4.50 + (10 * self.taxi.price_per_km)  # Flagfall + distance fare
        self.assertEqual(self.taxi.get_fare(), expected_fare)

    def test_str_method(self):
        """Test the string representation of the SilverServiceTaxi."""
        self.assertEqual(str(self.taxi),
                         "Silver Limo, fuel=200, odo=0, 0km on current fare, $2.46/km plus flagfall of $4.50")


if __name__ == "__main__":
    unittest.main()
