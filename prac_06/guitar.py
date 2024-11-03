class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2024  # Assuming the current year is 2024; you might want to dynamically fetch this value
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar1)
print(f"Age: {guitar1.get_age()} years")
print(f"Is vintage: {guitar1.is_vintage()}")