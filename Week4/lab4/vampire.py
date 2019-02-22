# This file provides the subclass Vampire of the super class Monster

import monster

class Vampire(monster.monster):
    def __init__(self, name, maxHealth):
        self.__name = name
        self.__health = maxHealth
        self.__maxHealth = maxHealth
        # self.name = "Drax the Vampire"

    def __str__(self):
        return "Flying Vampire"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "An emissary of darkness."

    def basicAttack(self, enemy):
        enemy.doDamage(5)

    def basicName(self):
        return "Scrape"

    def specialAttack(self, enemy):
        enemy.doDamage(15)

    def specialName(self):
        return "Bite"

    def defenseAttack(self, enemy):
        self.doDamage(-15)
        enemy.doDamage(1)

    def defenseName(self):
        return "Jump"

    def doDamage(self, damage):
        self.__health -= damage

    def getHealth(self):
        return self.__health

    def resetHealth(self):
        self.__health = self.__maxHealth
