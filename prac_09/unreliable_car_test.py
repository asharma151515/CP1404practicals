"""
CP1404/CP5632 Practical
Unreliable Car Test
"""


from unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("prius", 100, 10)
distance_drive = my_unreliable_car.drive(50)
print(f"Distance driven: {distance_drive} km")
print(my_unreliable_car)

