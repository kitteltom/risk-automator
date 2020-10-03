# Risk automator

Automates rolling dices in the board game 'Risk' to enable faster games. The players can simply invoke the script each time they fight for a country and move troops according to the result.

## How to use

Simply invoke the script with python like this:

```bash
python roll_the_dices.py -o 10 -l 4 -d 5
```

where `-o` refers to the initial number of offense troops in the attacking country, `-l` refers to the minimum number of offense troops that should be left in the attackers country after finishing the battle and `-d` refers to the initial number of defense troops in the defending country.
