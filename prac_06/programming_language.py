class Programming_language:

    def __init__(self, name, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def __str__(self):
        string = f"{self.name}, {self.typing} Typing, Reflection = " + str(self.reflection == "Yes")\
                 + f", First appeared in {self.year}"
        return string

    def getName(self):
        return self.name

    def is_dynamic(self):
        return self.typing == "Dynamic"
