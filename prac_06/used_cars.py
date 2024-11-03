"""CP1404/CP5632 Practical - Car class example."""

from car import Car # Ensure this import statement matches the name of your python file containing the Car class


def main():
    # Create a new Car object called "limo" with 100 units of fuel
    limo = Car(100, "Limo")

    # Add 20 more units of fuel to this new car object
    limo.add_fuel(20)

    # Print the amount of fuel in the car
    print(f"Limo has fuel: {limo.fuel}")

    # Attempt to drive the car 115 km
    driven_distance = limo.drive(115)
    print(f"Limo was able to drive {driven_distance} km.")

    # Print the car object to demonstrate the __str__ method
    print(limo)

class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0, name="Car"):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        name: str, name of the car
        """
        self.fuel = fuel
        self._odometer = 0
        self.name = name

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

if __name__ == "__main__":
    main()
