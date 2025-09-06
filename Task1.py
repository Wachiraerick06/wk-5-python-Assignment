# Base class
class Character:
    def __init__(self, name, age):
        self.name = name        # Public attribute
        self._age = age         # Protected attribute (encapsulation)

    def introduce(self):
        return f"My name is {self.name}, and I am {self._age} years old."


# Derived class (inherits from Character)
class Superhero(Character):
    def __init__(self, name, age, superpower, hero_name):
        super().__init__(name, age)   # Call the base class constructor
        self.superpower = superpower
        self.hero_name = hero_name

    def reveal_identity(self):
        return f"I am {self.hero_name}, master of {self.superpower}!"

    # Polymorphism example: overriding introduce()
    def introduce(self):
        return f"I am {self.hero_name}, but secretly {self.name}."


# Another subclass for variety
class Villain(Character):
    def __init__(self, name, age, evil_plan):
        super().__init__(name, age)
        self.evil_plan = evil_plan

    def introduce(self):
        return f"I am {self.name}, and I plan to {self.evil_plan}!"


# Example usage
hero1 = Superhero("iron man", 50, "Rich and intelligence", "tony stark")
hero2 = Superhero("batman", 40, "Rich and intelligence", "bruce wayne")
villain = Villain("Thanos", 45, "take over the world")

print(hero1.introduce())        # Polymorphism in action
print(hero1.reveal_identity())
print(hero2.introduce())        # Polymorphism in action
print(hero2.reveal_identity())
print(villain.introduce())
