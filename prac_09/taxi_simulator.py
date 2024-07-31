from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    # Create a list of taxi objects
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    menu = "(q)uit, (c)hoose taxi, (d)rive"

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            # Choose a taxi
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                distance_driven = current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                bill += fare
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                print(f"Bill to date: ${bill:.2f}")
        else:
            print("Invalid option")

    print(f"Total trip cost: ${bill:.2f}")


if __name__ == "__main__":
    main()
