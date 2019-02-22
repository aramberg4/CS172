from monster import monster


class Lich(monster):
    def __init__(self, name, maxHealth):
        self.__name = name
        self.__healthLevel = maxHealth
        self.__maxHealth = maxHealth

    def __str__(self):
        return "Lich"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "An undead spellcaster of great power."

    def basicAttack(self, enemy):
        enemy.doDamage(12)

    def basicName(self):
        return "Ray of Frost"

    def defenseAttack(self, enemy):
        self.doDamage(-5)
        enemy.doDamage(5)

    def defenseName(self):
        return "Soul drain"

    def specialAttack(self, enemy):
        enemy.doDamage(40)

    def specialName(self):
        return "Finger of Death"

    def getHealth(self):
        return self.__healthLevel

    def doDamage(self, damage):
        self.__healthLevel -= damage

    def resetHealth(self):
        self.__healthLevel = self.__maxHealth
