# This file provides the subclass Vampire of the super class Monster

import monster


class GiantCircle(monster.monster):
    def __init__(self, name, health):
        self.__health = health
        self.__name = name
        self.__maxHealth = health
        # self.name = "Steve the Giant Circle"

    def __str__(self):
        return "Giant Circle"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "A gigantic circle of deep circumspection. It radiates power."

    def basicAttack(self, enemy):
        enemy.doDamage(0)

    def basicName(self):
        return "Contemplate"

    def specialAttack(self, enemy):
        enemy.doDamage(75)

    def specialName(self):
        return "Roll Towards"

    def defenseAttack(self, enemy):
        self.doDamage(-5)
        enemy.doDamage(1)

    def defenseName(self):
        return "Roll Away"

    def doDamage(self, damage):
        self.__health -= damage

    def getHealth(self):
        return self.__health

    def resetHealth(self):
        self.__health = self.__maxHealth
