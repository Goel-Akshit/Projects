from Classes.colors import BColors
from Classes.person import Person
# from Classes.funlib import showlist,player_choosed
import random

def player_choosed(player_choice):
    if player_choice == 1:
       Reim = Person(739, 220, abilities["Reim"],damage[0])
       return Reim

    elif player_choice == 2:
       Sky = Person(650, 380, abilities["Sky"],damage[2])
       return Sky

    elif player_choice == 3:
       Vox = Person(695, 200, abilities["Vox"],damage[1])
       return Vox

    else:
        print("please chooce a option from the current list")
        return None

def showlist(array):
    j = 1
    for i in array:
        print( j,":",i)
        j += 1



players_list = ["Reim", "Sky", "Vox"]
abilities = {"Reim": ["WINTER SPIRE", "CHILL WINDS", "VALKYRIE"],
             "Vox": ["SONIC ZOOM", "PULSE", "WAIT FOR IT"],
             "Sky": ["FORWARD BARRAGE", "SURI STRIKE", "DEATH FROM ABOVE"]}
# in the form [energy_cost , damage]
damage = [{"WINTER SPIRE": [45, 70], "CHILL WINDS": [30, 60], "VALKYRIE": [50, 150]},
          {"SONIC ZOOM": [80,20], "PULSE": [40, 50], "WAIT FOR IT": [70,120]},
          {"FORWARD BARRAGE": [80,80], "SURI STRIKE": [40,30], "DEATH FROM ABOVE": [90,140]}]

print(BColors.Yellow + "===============================" + BColors.Endc)
print(BColors.Blue + BColors.Bold + "Welcom to my Vainglory:" + BColors.Endc+ "\n")
showlist(players_list)

player_choice = int(input("Enter Choice: "))
player = player_choosed(player_choice)
while player == None:
    player_choice = int(input("Enter Choice: "))
    player = player_choosed(player_choice)
print(BColors.Green + "player You choosed is:",players_list[player_choice - 1])
randomly = random.randint(1,3)
enemy = player_choosed(randomly)
print(BColors.Magenta + " your Enemy is:",players_list[randomly - 1] + BColors.Endc)


battle = True

while battle:

    if player.gethp() > 0 and enemy.gethp() > 0:
       attack =  player.choose_ability()
       enemy.sethp(attack)
       if(enemy.gethp() < 0):
        print(BColors.Green + BColors.Underline +  "You Defeated Enemy:" + BColors.Endc)
        battle = False
        break
       print(BColors.Blue + "enemy's health reduced to ",enemy.gethp(),"\n" + BColors.Endc)

       enemy_attack = enemy.enemy_chosed_ability(random.randint(1,3))
       player.sethp(enemy_attack)
       if(player.gethp() < 0):
        print(BColors.Cyan + BColors.Underline + " You Were Defeated" + BColors.Endc )
        battle = False
        break
       print(BColors.Red + "Your health reduced to ",player.gethp(),"\n"+ BColors.Endc)

    else:
        print(BColors.Yellow + "He He .... Close call" + BColors.Endc)
        battle = False
