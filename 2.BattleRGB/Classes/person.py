import random
from Classes.colors import BColors
import sys

class Person:

    def __init__(self, hp, ep, abilities, damage):
        self.hp = hp
        self.ep = ep
        self.epmax = ep
        self.abilities = abilities
        self.damage = damage
        self.magicBoost = 1

    @classmethod
    def showlist(self, array):
        j = 1
        for i in array:
            print( j,":",i)
            j += 1

    def is_available(self, cost):
        if (self.ep-cost) >= 0:
            self.ep -= cost
            return True
        else:
            return False


    def choose_ability(self):
        print(BColors.Yellow + BColors.Bold + "Choose ability" + BColors.Endc)
        self.showlist(self.abilities)
        ability_choosed = int(input("Enter Choice: "))
        ability = self.abilities[ability_choosed - 1]
        # check for ep of the ability
        ability_available = self.is_available(self.damage[ability][0])
        if ability_available:
            offense_high =  self.damage[ability][1] + 10
            offense_low = self.damage[ability][1] - 10
            attack = random.randint(offense_low, offense_high)
            print("Your choosed ability is:"+ BColors.Magenta, str(ability),BColors.Endc + "and its damage is:"+BColors.Green,str(attack) + BColors.Endc)
            print("your ability used energy",self.damage[ability][0],"energy left is",self.ep)
            return attack
        else:
            flag = False
            print("\nyour energy is",self.ep,"\n enegy cost of abilities is:")
            for i in self.damage:
                print(i,":",self.damage[i][0])
                if(self.damage[i][0] > self.ep):
                    flag = True

            if flag:
                print("\nOhh u can't use any ability due to low Energy .. Dont worry I have a energy boost for u")
                magic_boost = int(input("Press 1 to Boost:"))
                if magic_boost == 1 and self.magicBoost != 0:
                    self.ep = self.epmax//4
                    self.magicBoost -= 1
                    print("You are Boosted")
                    new_attack = self.choose_ability()
                    return new_attack
                else:
                    print("you cant be boosted")
                    print(BColors.Cyan + BColors.Underline + " You Were Defeated" + BColors.Endc )
                    sys.exit()

    def enemy_chosed_ability(self,random_choice):
        ability = self.abilities[random_choice - 1]
        offense_high =  self.damage[ability][1] + 10
        offense_low = self.damage[ability][1] - 10
        attack = random.randint(offense_low, offense_high)
        print("Enemy attcked You with",ability)
        return attack

    def gethp(self):
        return self.hp

    def getep(self):
        return self.ep

    def sethp(self,att):
        self.hp -= att

    def setep(self,energy):
        self.ep -= energy
