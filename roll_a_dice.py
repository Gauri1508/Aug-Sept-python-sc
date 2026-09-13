import random


class Dice:
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
       # print(f"({a},{b})")
        return (a, b)


dice = Dice()
print(dice.roll())
