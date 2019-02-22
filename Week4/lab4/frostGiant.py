from monster import monster


class FrostGiant(monster):
    def __init__(self, name, maxHealth):
        self.__name = name
        self.__healthLevel = maxHealth
        self.__maxHealth = maxHealth

    def __str__(self):
        return "Frost Giant"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "A giant from an arctic land."

    def basicAttack(self, enemy):
        enemy.doDamage(17)

    def basicName(self):
        return "Swing Club"

    def defenseAttack(self, enemy):
        self.doDamage(-20)

    def defenseName(self):
        return "Regenerate"

    def specialAttack(self, enemy):
        enemy.doDamage(20)

    def specialName(self):
        return "Ice Breath"

    def getHealth(self):
        return self.__healthLevel

    def doDamage(self, damage):
        self.__healthLevel -= damage

    def resetHealth(self):
        self.__healthLevel = self.__maxHealth
