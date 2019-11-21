# The Modern Python 3 Bootcamp - Colt Steele (Coding Exercise 81)


class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return f"{0} says: 'I heard monsters running around last night!"


villager = NPC("Bob", 100, 12)
print(
    f"""The villager's name is {villager.name}, their HP is {villager.hp} \
and their level is {villager.level}""")
villager.speak()
