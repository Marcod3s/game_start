class character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def __str__(self):
        return f"{self.name}'s health is {self.health}"

# player = character("name", 10)
# beast = character("beast", 15)
# class beast:
# def __init__(self, name, health):
# self.name = beast
# self.health = 15
# def __str__(self):
# return f"{self.name}'s health is {self.health}"
