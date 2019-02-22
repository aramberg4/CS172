# Monster Battle
# Authors: Earl Hyatt and Austin Ramberg
# Date: 2019 Jan. 31
# Description: Create instances of monsters from the classes included with
#              this file, and have them battle in a tournament.


# from monster import *
from lich import Lich
from frostGiant import FrostGiant
from vampire import Vampire
from giantCircle import GiantCircle
import random


# This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    # first reset everyone's health!
    m1.resetHealth()
    m2.resetHealth()

    # next print out who is battling
    print("Starting Battle Between")
    print(m1.getName(), ": ", m1.getDescription(), sep='')
    print(m2.getName(), ": ", m2.getDescription(), sep='')
    print('')

    # Whose turn is it?
    attacker = None
    defender = None

    # Select Randomly whether m1 or m2 is the initial attacker
    # to other is the initial definder
    if (random.randint(0, 1) == 0):
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1

    print(attacker.getName() + " goes first.")
    # Loop until either 1 is unconscious or timeout
    while (m1.getHealth() > 0 and m2.getHealth() > 0):
        # Determine what move the monster makes
        # Probabilities:
        #       60% chance of standard attack
        #       20% chance of defense move
        #       20% chance of special attack move

        # Pick a number between 1 and 100
        move = random.randint(1, 100)

        # It will be nice for output to record the damage done
        # before_health = defender.getHealth()

        # For each of these options, apply the appropriate attack and
        # print out who did what attack on whom
        if (move >= 1 and move <= 60):
            # Attacker uses basic attack on defender
            print(attacker.getName(), 'uses', attacker.basicName(), 'on',
                  defender.getName())
            attacker.basicAttack(defender)
        elif move >= 61 and move <= 80:
            # Defend!
            print(attacker.getName(), 'uses', attacker.defenseName(), 'on',
                  defender.getName())
            attacker.defenseAttack(defender)
        else:
            # Special Attack!
            print(attacker.getName(), 'uses', attacker.specialName(), 'on',
                  defender.getName())
            attacker.specialAttack(defender)

        # Swap attacker and defender
        attackerDummy = attacker
        attacker = defender
        defender = attackerDummy

        # Print the names and healths after this round
        print(m1.getName(), "at", m1.getHealth())
        print(m2.getName(), "at", m2.getHealth())
        print()  # add some spacing after the fight

    # Return who won
    if m1.getHealth() > m2.getHealth():
        print(m1.getName(), 'has defeated', m2.getName(), 'in battle!\n')
        return m1
    else:
        print(m2.getName(), 'has defeated', m1.getName(), 'in battle!\n')
        return m2


# ----------------------------------------------------
if __name__ == "__main__":
    # Every battle should be different, so we need to
    # start the random number generator somewhere "random".
    # With no input Python will set the seed

    random.seed()  # Use 0 as the test seed to maintain order.

    monster_list = [
        Lich("Lichenstein, Terror of the Earth", 100),
        FrostGiant("Frosty, the Abominable", 100),
        GiantCircle("Steve, the Great Circle", 300),
        Vampire("Drax, the Nightstalker", 100)
    ]
    random.shuffle(monster_list)

    score_list = [0, 0, 0, 0]

    for outer in range(0, 3):
        for inner in range(outer + 1, 4):
            winner = monster_battle(monster_list[outer], monster_list[inner])
            if winner == monster_list[outer]:
                score_list[outer] += 1
            else:
                score_list[inner] += 1

    # Print out who won.
    max = score_list[0]
    max_idx = 0
    for i in range(1, 4):
        if score_list[i] > max:
            max = score_list[i]
            max_idx = i

    # Print final scores.
    print(monster_list[max_idx].getName(), "wins the tournament!")
    print("Scores:")
    for mon, scr in zip(monster_list, score_list):
        print(mon.getName(), ': ', scr, sep='')
