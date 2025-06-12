class Item:
    def __init__(self, name, power=0):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name} (Guc: {self.power})"