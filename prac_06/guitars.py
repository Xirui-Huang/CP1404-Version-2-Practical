class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

def main():
    print("My guitars!")
    guitars = []

    # Uncomment for manual data entry
    # while True:
    #     name = input("Name: ")
    #     if not name:
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitars.append(Guitar(name, year, cost))
    #     print(f"{Guitar(name, year, cost)} added.\n")

    # Hardcoded data for testing
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()
