# Copyright 2020-present, Thomas Kittel
# All rights reserved.

import random
import argparse

"""
Automates rolling dices in the board game 'Risk' to enable faster games. 
The players can simply invoke the script each time they fight for a country
and move troops according to the result.
"""

# Parser for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--offense', type=int, default=4,
                    help='Initial number of offense troops.')
parser.add_argument('-l', '--limit', type=int, default=1,
                    help='Minimum number of offense troops that should be left in the attackers country.')
parser.add_argument('-d', '--defense', type=int, default=1,
                    help='Initial number of defense troops.')


def fight(num_offense_troops=4, offense_min=1, num_defense_troops=1):
    """
    Fights the fight between two countries and returns the remaining number
    of offense and defense troops in each country.

    :param num_offense_troops: Initial number of offense troops.
    :param offense_min: Minimum number of offense troops that should be left in the attackers country.
    :param num_defense_troops: Initial number of defense troops.
    :return: The remaining number of offense and defense troops in each country.
    """

    # Check the input
    if num_offense_troops < 2:
        raise ValueError('You need at least two offense troops to attack!')
    if offense_min < 1:
        raise ValueError('There must be at least one offense troop left in the county after the battle ended!')
    if num_defense_troops < 1:
        raise ValueError('Number of defense troops cannot be less than one!')
    
    # Play until one army is destroyed
    while num_offense_troops > offense_min and num_defense_troops > 0:
        # Choose the number of offense dices and roll them
        num_offense_dices = num_offense_troops - 1 if num_offense_troops < 4 else 3
        offense_result = roll(num_offense_dices)

        # Choose the number of defense dices and roll them
        num_defense_dices = 1 if num_defense_troops == 1 else choose_defense(offense_result)
        defense_result = roll(num_defense_dices)

        # Compare the results and decrease the number of troops
        num_battles = 2 if num_offense_dices > 1 and num_defense_dices > 1 else 1
        for battle in range(num_battles):
            if offense_result[battle] > defense_result[battle]:
                num_defense_troops -= 1
            else:
                num_offense_troops -= 1

    return num_offense_troops, num_defense_troops


def roll(num_dices):
    """
    Roll num_dices and sort them.

    :param num_dices: Number of dices to roll.
    :return: The result for each dices sorted in descending order.
    """
    result = [random.randint(1, 6) for _ in range(num_dices)]
    result.sort(reverse=True)
    return result


def choose_defense(offense_result):
    """
    Strategy for how to choose the number of dices the defense uses.

    :param offense_result: Result of the offense's dice roll.
    :return: Number of dices the defense uses.
    """
    if len(offense_result) == 1:
        return 2

    if offense_result[0] + offense_result[1] < 8:
        return 2

    return 1


if __name__ == '__main__':
    args = parser.parse_args()

    offense, defense = fight(args.offense, args.limit, args.defense)

    print('The fight just came to an end:')
    print('------------------------------')
    print('# Offense Troops left: %d' % offense)
    print('# Defense Troops left: %d' % defense)
