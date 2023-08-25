class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        string = f"{self.name} ({self.year}) : $ {str(self.cost)}"
        return string

    def get_age(self):
        return 2023 - int(self.year)

    def is_vintage(self):
        return self.get_age() >= 50
