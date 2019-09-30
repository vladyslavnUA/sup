import random
from random import choice

class Ability:
    def __init__(self, name, attackStrength):
        self.name = name
        self.attackStrength = attackStrength

        pass

    def attack(self):
        randomAttack = random.randint(0, self.attackStrength)
        return randomAttack
    
if __name__ == "__main__":
    #if you run this file from the terminal
    #this block is executed
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
