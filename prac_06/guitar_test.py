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

# Testing code
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 1000)

# Test get_age() method
guitar1_age = guitar1.get_age()
guitar2_age = guitar2.get_age()
print(f"Gibson L-5 CES get_age() - Expected 102. Got {guitar1_age}")
print(f"Another Guitar get_age() - Expected 11. Got {guitar2_age}")

# Test is_vintage() method
guitar1_vintage = guitar1.is_vintage()
guitar2_vintage = guitar2.is_vintage()
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar1_vintage}")
print(f"Another Guitar is_vintage() - Expected False. Got {guitar2_vintage}")
