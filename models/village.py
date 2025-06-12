class Village:
    def __init__(self, name, items=None):
        self.name = name
        self.items = items if items else []

    def __str__(self):
        item_names = ", ".join(item.name for item in self.items)
        return f"{self.name} Koyu → Esyalar: [{item_names}]"