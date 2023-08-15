import random
import time
import json

print("Hello! If you're newbie register at first")
print('/reg to register')
print('/log to login')

with open('users.txt') as json_file2:
    users = json.load(json_file2)
with open('data.txt') as stats1:
    data = json.load(stats1)


valid = 1
username = 0
lvl = 0
power = 1
money = 13
red_money = 0
tickets = 0
cloaks = 0
fragments_of_d2 = 0
fragments_of_ktn = 0
ancient_d2 = 0
attempts = 0
hp = 20
min_dmg = 3
max_dmg = 4
crit_ch = 0
crit_dmg = 0
evade = 0
l_kn = 1
l_arm = 1
l_mask = 0
l_cloak = 0
l_ktn = 0
luck = 1000
user_id = 0

#users.extend([1, 1337, 1, 'admin'])
#data.extend([1, 0, 0, 1, 13, 0, 20, 3, 4, 0, 0, 1, 1, 0, 0, 0, 0])


cost = [0, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 11000, 25000, 60000, 200000]
chance = [0, 90, 84, 78, 72, 66, 60, 55, 50, 45, 41, 37, 33, 29, 25]
rch = [0, 850, 750, 620, 660, 540, 460, 410, 340, 300, 260, 210, 160, 120, 90]
ch_up = [0, 300, 300, 200, 150, 150, 130, 120, 120, 120, 110, 110, 100, 100, 90]
powerup = [0, 1, 2, 3, 5, 8, 13, 28, 60, 125, 250, 450, 800, 1500, 5000]
min_dmg_up = [0, 2, 3, 5, 8, 14, 23, 40, 77, 133, 210, 333, 555, 880, 1400]
max_dmg_up = [0, 3, 4, 7, 10, 16, 26, 43, 82, 140, 222, 355, 588, 990, 1600]
hp_up = [0, 10, 20, 35, 65, 115, 220, 400, 750, 1300, 2400, 4500, 8000, 15000, 25000]
cost_mask = [666, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 14000, 16000, 18000, 20000, 22000,
             24000, 26000, 28000, 30000]
crit_ch_up = [13, 2, 2, 2, 2, 2, 2, 2, 2, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 10]
crit_dmg_up = [25, 15, 15, 15, 15, 15, 15, 15, 15, 25, 15, 15, 15, 15, 15, 15, 15, 15, 15, 25]
powerup_mask = [30, 20, 20, 20, 20, 20, 20, 20, 20, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 1000]
chance_mask = [1000, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
rch_mask = [1000, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
ch_up_mask = [0, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
evade_up = [13, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
cloaks_frag = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
cost_cloak = [666, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 14000, 16000, 18000, 20000, 22000,
              24000, 26000, 28000, 30000]
powerup_cloak = [1000, 250, 250, 250, 250, 250, 250, 250, 250, 250, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
                 1000, 1000]
chance_cloak = [1000, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60]
rch_cloak = [1000, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
ch_up_cloak = [0, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
enemy_name = ["Fly", "Cockroach", "Frog", "Spider", "Snake", "Puppy", "Goat", "Black Panda", "Red Panda",
              "the King Panda", "Foxie"]
enemy_hp = [10, 50, 200, 400, 2000, 5000, 8000, 20000, 15000, 50000, 80000]
enemy_dmg = [2, 7, 15, 50, 200, 700, 1100, 1700, 3000, 5000, 6666]
enemy_crit_ch = [0, 0, 0, 0, 0, 0, 0, 0, 25, 13, 25]
enemy_crit_dmg = [0, 0, 0, 0, 0, 0, 0, 0, 333, 500, 300]
money_gain_mim = [20, 40, 70, 130, 300, 444, 700, 1000, 2000, 4000, 0]
money_gain_max = [30, 65, 120, 200, 450, 777, 1500, 5000, 12000, 30000, 0]
red_money_gain_mim = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
red_money_gain_max = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
power_rcmd = [1, 10, 32, 70, 300, 900, 1300, 3000, 7000, 15000, 25000]
ch_drop_cloak = [0, 0, 0, 0, 0, 0, 1, 2, 3, 5, 7]
ch_drop_fragments_of_d2 = [0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 25]
ch_drop_fragments_of_ktn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13]

ticket_cost = 50000


def shop():
    if lvl >= 8:
        print("###############################################")
        print("You just entered the shop!")
        print("Check out assortment")
        print("/tick to buy a lottery ticket")
        print("/a_frag to buy Ancient fragment")
        print("###############################################")
    else:
        print("You can't enter shop before 8 level")


def buy_ticket():
    global money
    global tickets
    if lvl >= 8:
        print("Do you want to buy a lottery ticket?")
        print("Cost is " + str(ticket_cost))
        askin = input("Type yes or no:")
        if "y" in askin:
            money -= ticket_cost
            tickets += 1
            print("You bought a ticket")
        else:
            print("Returning back...")
    else:
        print("You can't enter shop before 8 level")


def ticket():
    global tickets
    global luck
    if tickets >= 1:
        luck -= 100
        tickets -= 1
        print("Luck is on your side!")
    else:
        print("You don't have any tickets")


#def d2():


while True:
    command = input()
    if user_id >= 1:
        if '/help' in command:
            print("/g (level number) to fight")
            print("/kn to increase your DMG")
            print("/arm to increase your HP")
            print("/mask to upgrade Mask")
            print("/cloak to upgrade Cloak")
            print("/anc to chain fragments")
            print("/check to check out your stats")
            print("/inv to check out your inventory")
            print("/out to log out from account")

        elif '/reg' in command:
            print("You can't register while you're in account")
        elif '/log' in command:
            if user_id >= 1:
                print("You've logged in already")
        elif '/out' in command:
            user_id = 0
            with open('data.txt') as stats3:
                data = json.load(stats3)
                for ht in data:
                    valid = data[0]
                    username = data[1]
                    lvl = data[2]
                    power = data[3]
                    money = data[4]
                    red_money = data[5]
                    tickets = data[6]
                    cloaks = data[7]
                    fragments_of_d2 = data[8]
                    fragments_of_ktn = data[9]
                    ancient_d2 = data[10]
                    attempts = data[11]
                    hp = data[12]
                    min_dmg = data[13]
                    max_dmg = data[14]
                    crit_ch = data[15]
                    crit_dmg = data[16]
                    evade = data[17]
                    l_kn = data[18]
                    l_arm = data[19]
                    l_mask = data[20]
                    l_cloak = data[21]
                    l_ktn = data[22]
                    luck = data[23]
                    user_id = data[24]
            print("You've logged out")
        elif '/shop' in command:
            shop()
        elif '/tick' in command:
            buy_ticket()
        elif '/ticket' in command:
            ticket()
        elif '/id' in command:
            print(str(user_id))
        elif '/inv' in command:
            if cloaks >= 1:
                print(str(cloaks) + " Cloak fragments")
                if l_cloak >= 1:
                    print("You can use it to upgrade Cloak by /cloak")
                else:
                    print("You can use it to get Cloak by /cloak")
            if fragments_of_d2 >= 1:
                print(str(fragments_of_d2) + " Ancient fragments")
                print("You can make an ancient object using them by /anc")
            if ancient_d2 >= 1:
                print(str(ancient_d2) + " Ancient Relics")
                print("You can use it to unleash ancient power of your knife /rel")
            if fragments_of_ktn >= 1:
                print(str(fragments_of_ktn) + " Katana fragments")
                print("You can make an Katana using them by /anc")
            if tickets >= 1:
                print(str(tickets) + " lottery tickets")
                print("You can use it to upgrade your success chance by /ticket")
            if cloaks == 0 and fragments_of_d2 == 0 and ancient_d2 == 0 and fragments_of_ktn == 0:
                print("Your inventory is empty in the moment!")
        elif '/check' in command:
            print("###############################################")
            print(str(lvl) + " levels passed")
            print(str(power) + " power")
            print(str(money) + " money")
            if red_money >= 1:
                print(str(red_money) + " red money")
            print(str(attempts) + " attempts")
            print(str(hp) + " HP")
            print(str(min_dmg) + "-" + str(max_dmg) + " DMG")
            if l_mask >= 1:
                print(str(crit_ch) + " crit chance")
                print(str(crit_dmg) + " crit DMG multiplier")
            if l_cloak >= 1:
                print(str(evade) + " evade chance")
            if l_kn < len(min_dmg_up):
                print(str(cost[l_kn]) + " money for Knife lvl " + str(l_kn + 1) + "!")
            elif l_kn == len(min_dmg_up):
                print("Your Knife is on maximum!")
            if l_arm < len(hp_up):
                print(str(cost[l_arm]) + " money for Armor lvl " + str(l_arm + 1) + "!")
            elif l_arm == len(hp_up):
                print("Your Armor is on maximum!")
            if l_mask == 0:
                if l_kn <= 6:
                    print("Enhance your knife to 7 level to buy Mask!")
                else:
                    print("Buy Mask for 666 money!")
            elif l_mask >= 1:
                if l_mask < len(crit_ch_up):
                    print(str(cost_mask[l_mask]) + " money for Mask lvl " + str(l_mask + 1) + "!")
                elif l_mask == len(crit_ch_up):
                    print("Your Mask is on maximum!")
            if l_cloak >= 1:
                if l_cloak < len(evade_up):
                    print(str(cloaks_frag[l_cloak]) + " cloak fragments for Cloak lvl " + str(l_cloak + 1) + "!")
                elif l_cloak == len(evade_up):
                    print("Your Cloak is on maximum!")
            print("###############################################")
        elif "/kn" in command:
            if l_kn < len(min_dmg_up):
                if money >= cost[l_kn]:
                    print("Upgrade to level " + str(l_kn + 1) + "?")
                    print("Cost is " + str(cost[l_kn]))
                    print("Success chance is " + str(chance[l_kn]) + "%")
                    askin = input("Type yes or no:")
                    if "y" in askin:
                        money -= cost[l_kn]
                        print('Enchanting! 3...')
                        time.sleep(1)
                        print('2...')
                        time.sleep(1)
                        print('1...')
                        time.sleep(1)
                        x = random.randint(1, luck)
                        if x <= rch[l_kn]:
                            luck = 1000
                            min_dmg += min_dmg_up[l_kn]
                            max_dmg += max_dmg_up[l_kn]
                            power += powerup[l_kn]
                            l_kn += 1
                            print("Upgraded! Knife is level " + str(l_kn))
                            print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                        else:
                            luck -= ch_up[l_kn]
                            print("Fail... Your Knife's level is still " + str(l_kn))
                        print('Wanna try one more time?')
                    else:
                        print("Returning back")
                        continue
                else:
                    print("Not enough money!")
            else:
                print("Your Knife is maximum!")
        elif "/arm" in command:
            if l_arm < len(hp_up):
                if money >= cost[l_arm]:
                    print("Upgrade to level " + str(l_arm + 1) + "?")
                    print("Cost is " + str(cost[l_arm]))
                    print("Success chance is " + str(chance[l_arm]) + "%")
                    askin = input("Type yes or no:")
                    if "y" in askin:
                        money -= cost[l_arm]
                        print('Enchanting! 3...')
                        time.sleep(1)
                        print('2...')
                        time.sleep(1)
                        print('1...')
                        time.sleep(1)
                        x = random.randint(1, luck)
                        if x <= rch[l_arm]:
                            luck = 1000
                            hp += hp_up[l_arm]
                            power += powerup[l_arm]
                            l_arm += 1
                            print("Upgraded! Armor is level " + str(l_arm))
                            print("Your HP is " + str(hp))
                        else:
                            luck -= ch_up[l_arm]
                            print("Fail... Your Armor's level is still " + str(l_arm))
                        print('Wanna try one more time?')
                    else:
                        print("Returning back")
                        continue
                else:
                    print("Not enough money!")
            else:
                print("Your Armor is maximum!")
        elif "/mask" in command:
            if l_kn >= 7:
                if l_mask < len(crit_ch_up):
                    if money >= cost_mask[l_mask]:
                        if l_mask >= 1:
                            print("Upgrade to level " + str(l_mask + 1) + "?")
                            print("Cost is " + str(cost_mask[l_mask]))
                            print("Success chance is " + str(chance_mask[l_mask]) + "%")
                        elif l_mask == 0:
                            print("Do you wanna buy a mask?")
                            print("Cost is " + str(cost_mask[l_mask]))
                        askin = input("Type yes or no:")
                        if "y" in askin:
                            money -= cost_mask[l_mask]
                            if l_mask == 0:
                                print('Crafting! 3...')
                            elif l_mask >= 1:
                                print('Enchanting! 3...')
                            time.sleep(1)
                            print('2...')
                            time.sleep(1)
                            print('1...')
                            time.sleep(1)
                            x = random.randint(1, luck)
                            if x <= rch_mask[l_mask]:
                                luck = 1000
                                crit_ch += crit_ch_up[l_mask]
                                crit_dmg += crit_dmg_up[l_mask]
                                power += powerup_mask[l_mask]
                                l_mask += 1
                                if l_mask == 1:
                                    print("You just bought Mask!")
                                elif l_mask >= 2:
                                    print("Upgraded! Mask is level " + str(l_mask))
                                print("Your crit chance is " + str(crit_ch))
                                print("Your crit damage is " + str(crit_dmg))
                            else:
                                luck -= ch_up_mask[l_mask]
                                print("Fail... Your Mask's level is still " + str(l_mask))
                            if l_mask >= 2 or luck < 1000:
                                print('Wanna try one more time?')
                        else:
                            print("Returning back")
                            continue
                    else:
                        print("Not enough money!")
                else:
                    print("Your Mask is maximum!")
            else:
                print("You cannot buy mask until your knife is level 7!")
        elif "/cloak" in command:
            if cloaks >= cloaks_frag[l_cloak]:
                if l_cloak < len(evade_up):
                    if money >= cost_cloak[l_cloak]:
                        if l_cloak >= 1:
                            print("Upgrade to level " + str(l_cloak + 1) + "?")
                            print("Need " + str(cloaks_frag[l_cloak]) + " fragments")
                            print("Cost is " + str(cost_cloak[l_cloak]))
                            print("Success chance is " + str(chance_cloak[l_cloak]) + "%")
                        elif l_cloak == 0:
                            print("Do you wanna buy a Cloak?")
                            print("Cost is " + str(cost_cloak[l_cloak]))
                        askin = input("Type yes or no:")
                        if "y" in askin:
                            money -= cost_cloak[l_cloak]
                            cloaks -= cloaks_frag[l_cloak]
                            if l_cloak == 0:
                                print('Crafting! 3...')
                            elif l_cloak >= 1:
                                print('Enchanting! 3...')
                            time.sleep(1)
                            print('2...')
                            time.sleep(1)
                            print('1...')
                            time.sleep(1)
                            x = random.randint(1, luck)
                            if x <= rch_cloak[l_cloak]:
                                luck = 1000
                                evade += evade_up[l_cloak]
                                power += powerup_cloak[l_cloak]
                                l_cloak += 1
                                if l_cloak == 1:
                                    print("You just bought Cloak!")
                                elif l_cloak >= 2:
                                    print("Upgraded! Cloak is level " + str(l_cloak))
                                print("Your evade chance is " + str(evade))
                            else:
                                luck -= ch_up_cloak[l_cloak]
                                print("Fail... Your Cloak's level is still " + str(l_cloak))
                            if l_cloak >= 2 or luck < 1000:
                                print('Wanna try one more time?')
                        else:
                            print("Returning back")
                            continue
                    else:
                        print("Not enough money!")
                else:
                    print("Your Cloak is maximum!")
            else:
                print("You don't have enough cloak fragments yet")
        elif '/anc' in command:
            anc1 = []
            rel = ["Acnient Relic", fragments_of_d2, ancient_d2]
            ktn = ["Katana", fragments_of_ktn, l_ktn]
            if '/anc rel' in command:
                anc1 = rel
            elif '/anc ktn' in command:
                anc1 = ktn
            elif '/anc' in command:
                if fragments_of_d2 >= 4:
                    print("/rel to Relic")
                if fragments_of_ktn >= 4:
                    print("/ktn to Katana")
                ancask = input("What do you want to chain?")
                if 'rel' in ancask:
                    anc1 = rel
                elif 'ktn' in ancask:
                    anc1 = ktn
            if anc1[1] >= 4:
                print("Try to chain together " + str(anc1[0]) + " fragments?")
                print("Cost is 1000")
                print("Success chance is very low")
                askin = input("Type yes or no:")
                if "y" in askin:
                    anc1[1] -= 4
                    money -= 1000
                    print('Chaining! 3...')
                    time.sleep(1)
                    print('2...')
                    time.sleep(1)
                    print('1...')
                    time.sleep(1)
                    x = random.randint(1, luck)
                    if x <= 30:
                        luck = 1000
                        anc1[2] += 1
                        print("Chained! Now you have " + str(anc1[0]))
                        print("You can use it to unleash ancient power of your knife")
                    else:
                        luck -= 20
                        print("Fail... You lost your fragments for nothing")
                    if anc1[0] == "Acnient Relic":
                        fragments_of_d2 = anc1[1]
                        ancient_d2 = anc1[2]
                    elif anc1[0] == "Katana":
                        fragments_of_ktn = anc1[1]
                        l_ktn = anc1[2]


                else:
                    print("Returning back")
                    continue
            elif anc1[1] < 4:
                print("Collect 4 fragments!")
        elif '/g auto' in command:
            moneyauto = 0
            red_moneyauto = 0
            cloak_auto = 0
            fragments_of_d2_auto = 0
            fragments_of_ktn_auto = 0
            for jsd in range(1, lvl * 2):
                level = random.randint(lvl - 3, lvl) - 1
                if level < 0:
                    level = 0
                if lvl <= level + 2:
                    ehp = enemy_hp[level]
                    your_hp = hp
                    moneyg = random.randint(money_gain_mim[level], money_gain_max[level])
                    moneyg += int(moneyg * lvl / 10)
                    red_moneyg = random.randint(red_money_gain_mim[level], red_money_gain_max[level])
                    red_moneyg += int(red_moneyg * (lvl - 10) / 10)
                    print("###############################################")
                    print('Your opponent is ' + str(enemy_name[level]) + '!')
                    print('HP = ' + str(ehp) + '/' + str(enemy_hp[level]))
                    print('DMG = ' + str(enemy_dmg[level]))
                    print("Recommended power is " + str(power_rcmd[level]))
                    print("###############################################")
                    time.sleep(1.6)
                    attempts += 1
                    while your_hp >= 1 and ehp >= 1:
                        dmg = random.randint(int(min_dmg), int(max_dmg))
                        crit = random.randint(1, 100)
                        if crit <= crit_ch:
                            dmg += dmg * crit_dmg / 100
                            dmg = int(dmg)
                        ehp -= dmg
                        print("You're hitting with " + str(dmg) + " DMG! " + str(ehp) + "/" + str(enemy_hp[level]))
                        time.sleep(0.6)
                        if ehp <= 0:
                            if lvl == level:
                                lvl += 1
                            money += moneyg
                            moneyauto += moneyg
                            red_money += red_moneyg
                            red_moneyauto += red_moneyg
                            print("###############################################")
                            if moneyg >= 1:
                                print("You won and got " + str(moneyg) + " money!")
                            if red_moneyg >= 1:
                                print("You got rare " + str(red_moneyg) + " red money!")
                            ch_cloak = random.randint(1, 100)
                            if ch_cloak <= ch_drop_cloak[level]:
                                cloaks += 1
                                cloak_auto += 1
                                if cloaks == 1:
                                    print("You just found a rare Cloak fragment!")
                                if cloaks >= 2:
                                    print("You just found a rare Cloak fragment!")
                                    print("Now you have " + str(cloaks) + " cloak fragments")
                            ch_fragments_of_d2 = random.randint(1, 100)
                            if ch_fragments_of_d2 <= ch_drop_fragments_of_d2[level]:
                                fragments_of_d2 += 1
                                fragments_of_d2_auto += 1
                                print("You just found an ancient fragment!")
                                print("Now you have " + str(fragments_of_d2) + " fragments")
                            ch_fragments_of_ktn = random.randint(1, 100)
                            if ch_fragments_of_ktn <= ch_drop_fragments_of_ktn[level]:
                                fragments_of_ktn += 1
                                fragments_of_ktn_auto += 1
                                print("You just found an Katana fragment!")
                                print("Now you have " + str(fragments_of_ktn) + " fragments")
                            print("###############################################")
                            time.sleep(0.6)
                            break
                        edmg = enemy_dmg[level]
                        enemy_crit = random.randint(1, 100)
                        if enemy_crit <= enemy_crit_ch[level]:
                            edmg += enemy_dmg[level] * enemy_crit_dmg[level] / 100
                            edmg = int(edmg)
                        evasion = random.randint(1, 100)
                        if evasion <= evade:
                            print("You just evaded!")
                        elif evasion > evade:
                            your_hp -= edmg
                            print(str(enemy_name[level]) + "'s biting you with " + str(edmg) + " DMG! " + str(
                                    your_hp) + "/" + str(hp))
                        time.sleep(0.6)
                        if your_hp <= 0:
                            print("###############################################")
                            print("You lost!")
                            print("###############################################")
                            time.sleep(0.6)
                            break
                else:
                    moneyg = random.randint(money_gain_mim[level], money_gain_max[level])
                    moneyg += int(moneyg * lvl / 10)
                    red_moneyg = random.randint(red_money_gain_mim[level], red_money_gain_max[level])
                    red_moneyg += int(red_moneyg * (lvl - 10) / 10)
                    money += moneyg
                    moneyauto += moneyg
                    red_money += red_moneyg
                    red_moneyauto += red_moneyg
                    print("###############################################")
                    print("Your opponent ran away in fear without a fight!")
                    if moneyg >= 1:
                        print("You won and got " + str(moneyg) + " money!")
                    if red_moneyg >= 1:
                        print("You got rare " + str(red_moneyg) + " red money!")
                    ch_cloak = random.randint(1, 100)
                    if ch_cloak <= ch_drop_cloak[level]:
                        cloaks += 1
                        cloak_auto += 1
                        if cloaks == 1:
                            print("You just found a rare Cloak fragment!")
                        if cloaks >= 2:
                            print("You just found a rare Cloak fragment!")
                            print("Now you have " + str(cloaks) + " cloak fragments")
                    ch_fragments_of_d2 = random.randint(1, 100)
                    if ch_fragments_of_d2 <= ch_drop_fragments_of_d2[level]:
                        fragments_of_d2_auto += 1
                        fragments_of_d2 += 1
                        print("You just found an ancient fragment!")
                        print("Now you have " + str(fragments_of_d2) + " fragments")
                    ch_fragments_of_ktn = random.randint(1, 100)
                    if ch_fragments_of_ktn <= ch_drop_fragments_of_ktn[level]:
                        fragments_of_ktn += 1
                        fragments_of_ktn_auto += 1
                        print("You just found an Katana fragment!")
                        print("Now you have " + str(fragments_of_ktn) + " fragments")
                    print("###############################################")
                    time.sleep(0.6)
            else:
                print("###############################################")
                print("Auto battle ended")
                print("You've gained total " + str(moneyauto) + " money")
                if red_moneyauto >= 1:
                    print("You've gained total " + str(red_moneyauto) + " rare red money!")
                if cloak_auto >= 1:
                    if cloaks == 1:
                        print("You just found a rare Cloak fragment!")
                    if cloaks >= 2:
                        print("You just found a rare Cloak fragment!")
                        print("Now you have " + str(cloaks) + " cloak fragments")
                if fragments_of_d2_auto >= 1:
                    print("You just found " + str(fragments_of_d2_auto) + " ancient fragments!")
                    print("Now you have " + str(fragments_of_d2) + " fragments")
                if fragments_of_ktn_auto >= 1:
                    print("You just found " + str(fragments_of_ktn_auto) + " Katana fragments!")
                    print("Now you have " + str(fragments_of_ktn) + " fragments")
                print("###############################################")
        elif '/g' in command:
            if '2' in command:
                level = 1
            elif '3' in command:
                level = 2
            elif '4' in command:
                level = 3
            elif '5' in command:
                level = 4
            elif '6' in command:
                level = 5
            elif '7' in command:
                level = 6
            elif '8' in command:
                level = 7
            elif '9' in command:
                level = 8
            elif '10' in command:
                level = 9
            elif '11' in command:
                level = 10
            elif '1' in command:
                level = 0
            elif '/g' in command:
                print("Please choose level")
                if lvl <= 9:
                    print("Available from 1 to " + str(lvl + 1))
                else:
                    print("Available from 1 to 10")
                levask = input()
                if '1' in levask:
                    level = 0
                elif '2' in levask:
                    level = 1
                elif '3' in levask:
                    level = 2
                elif '4' in levask:
                    level = 3
                elif '5' in levask:
                    level = 4
                elif '6' in levask:
                    level = 5
                elif '7' in levask:
                    level = 6
                elif '8' in levask:
                    level = 7
            if lvl >= level:
                ehp = enemy_hp[level]
                your_hp = hp
                moneyg = random.randint(money_gain_mim[level], money_gain_max[level])
                red_moneyg = random.randint(red_money_gain_mim[level], red_money_gain_max[level])
                print("###############################################")
                print('Your opponent is ' + str(enemy_name[level]) + '!')
                print('HP = ' + str(ehp) + '/' + str(enemy_hp[level]))
                print('DMG = ' + str(enemy_dmg[level]))
                print("Recommended power is " + str(power_rcmd[level]))
                print("###############################################")
                time.sleep(1.6)
                attempts += 1
                while your_hp >= 1 and ehp >= 1:
                    dmg = random.randint(int(min_dmg), int(max_dmg))
                    crit = random.randint(1, 100)
                    if crit <= crit_ch:
                        dmg += dmg * crit_dmg / 100
                        dmg = int(dmg)
                    ehp -= dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(ehp) + "/" + str(enemy_hp[level]))
                    time.sleep(1.3)
                    if ehp <= 0:
                        if lvl == level:
                            lvl += 1
                        money += moneyg
                        red_money += red_moneyg
                        print("###############################################")
                        if moneyg >= 1:
                            print("You won and got " + str(moneyg) + " money!")
                        if red_moneyg >= 1:
                            print("You got rare " + str(red_moneyg) + " red money!")
                        ch_cloak = random.randint(1, 100)
                        if ch_cloak <= ch_drop_cloak[level]:
                            cloaks += 1
                            if cloaks == 1:
                                print("You just found a rare Cloak fragment!")
                            if cloaks >= 2:
                                print("You just found a rare Cloak fragment!")
                                print("Now you have " + str(cloaks) + " cloak fragments")
                        ch_fragments_of_d2 = random.randint(1, 100)
                        if ch_fragments_of_d2 <= ch_drop_fragments_of_d2[level]:
                            fragments_of_d2 += 1
                            print("You just found an ancient fragment!")
                            print("Now you have " + str(fragments_of_d2) + " fragments")
                        ch_fragments_of_ktn = random.randint(1, 100)
                        if ch_fragments_of_ktn <= ch_drop_fragments_of_ktn[level]:
                            fragments_of_ktn += 1
                            fragments_of_ktn_auto += 1
                            print("You just found an Katana fragment!")
                            print("Now you have " + str(fragments_of_ktn) + " fragments")
                        print("###############################################")
                        break
                    edmg = enemy_dmg[level]
                    enemy_crit = random.randint(1, 100)
                    if enemy_crit <= enemy_crit_ch[level]:
                        edmg += enemy_dmg[level] * enemy_crit_dmg[level] / 100
                        edmg = int(edmg)
                    evasion = random.randint(1, 100)
                    if evasion <= evade:
                        print("You just evaded!")
                    elif evasion > evade:
                        your_hp -= edmg
                        print(str(enemy_name[level]) + "'s biting you with " + str(edmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                    if your_hp <= 0:
                        print("###############################################")
                        print("You lost!")
                        print("###############################################")
                        break
            else:
                print("First pass previous levels!")
        else:
            print('Wrong command!')
        if user_id in data:
            statsindex = data.index(user_id)
            statsindex += 1
            if statsindex // 25:
                for trf in data:
                    data[statsindex - 25] = valid
                    data[statsindex - 24] = username
                    data[statsindex - 23] = lvl
                    data[statsindex - 22] = power
                    data[statsindex - 21] = money
                    data[statsindex - 20] = red_money
                    data[statsindex - 19] = tickets
                    data[statsindex - 18] = cloaks
                    data[statsindex - 17] = fragments_of_d2
                    data[statsindex - 16] = fragments_of_ktn
                    data[statsindex - 15] = ancient_d2
                    data[statsindex - 14] = attempts
                    data[statsindex - 13] = hp
                    data[statsindex - 12] = min_dmg
                    data[statsindex - 11] = max_dmg
                    data[statsindex - 10] = crit_ch
                    data[statsindex - 9] = crit_dmg
                    data[statsindex - 8] = evade
                    data[statsindex - 7] = l_kn
                    data[statsindex - 6] = l_arm
                    data[statsindex - 5] = l_mask
                    data[statsindex - 4] = l_cloak
                    data[statsindex - 3] = l_ktn
                    data[statsindex - 2] = luck
                    data[statsindex - 1] = user_id
                with open('data.txt', 'w') as xfile:
                    json.dump(data, xfile)
        else:
            user_id = 0
            with open('data.txt') as stats2:
                data = json.load(stats2)
                for gt in data:
                    valid = data[0]
                    username = data[1]
                    lvl = data[2]
                    power = data[3]
                    money = data[4]
                    red_money = data[5]
                    tickets = data[6]
                    cloaks = data[7]
                    fragments_of_d2 = data[8]
                    fragments_of_ktn = data[9]
                    ancient_d2 = data[10]
                    attempts = data[11]
                    hp = data[12]
                    min_dmg = data[13]
                    max_dmg = data[14]
                    crit_ch = data[15]
                    crit_dmg = data[16]
                    evade = data[17]
                    l_kn = data[18]
                    l_arm = data[19]
                    l_mask = data[20]
                    l_cloak = data[21]
                    l_ktn = data[22]
                    luck = data[23]
                    user_id = data[24]
            print("You've logged out")
    else:
        if '/reg' in command:
            if user_id == 0:
                print('Choose login and password')
                registr = input('Login:')
                if type(registr) is str:
                    if len(registr) >= 3:
                        relogin = registr
                        registr = input('Password:')
                        if type(registr) is str:
                            if len(registr) >= 3:
                                user_id = random.randint(1, 10000)
                                while user_id in data:
                                    user_id = random.randint(1, 10000)
                                users.append(relogin)
                                users.append(registr)
                                users.append(user_id)
                                registr = input('Name:')
                                if type(registr) is str:
                                    users.append(registr)
                                    username = registr
                                    with open('users.txt', 'w') as stats3:
                                        json.dump(users, stats3)
                                    print('Registration is successful')

                                    data.extend(
                                        [valid, username, lvl, power, money, red_money, tickets, cloaks, fragments_of_d2, fragments_of_ktn, ancient_d2, attempts, hp, min_dmg, max_dmg, crit_ch,
                                         crit_dmg, evade, l_kn, l_arm, l_mask, l_cloak, l_ktn, luck, user_id])
                                    with open('data.txt', 'w') as outfile:
                                        json.dump(data, outfile)
                                    print("Hello! This is my first easy-made game!")
                                    print("/help to get help about gameplay")
                                else:
                                    print('Incorrect format')

                            else:
                                print('Too short! At least 3 characters')
                        else:
                            print('Incorrect format')
                    else:
                        print('Too short! At least 3 characters')
                else:
                    print('Incorrect format')
            else:
                print("You can't register while you're in account")
        elif '/log' in command:
            print('Enter your login and password')
            login = input('Login:')
            if type(login) is str:
                if login in users:
                    index = users.index(login)
                    if index // 4:
                        password = input('Password:')
                        if type(password) is str:
                            if password in users and users.index(password) == index + 1:
                                user_id_reg = users[index + 2]
                                if user_id_reg in data:
                                    statsindex = data.index(user_id_reg)
                                    statsindex += 1
                                    if statsindex // 25:
                                        with open('data.txt') as stats1:
                                            data = json.load(stats1)
                                            for ig in data:
                                                valid = data[statsindex - 25]
                                                username = data[statsindex - 24]
                                                lvl = data[statsindex - 23]
                                                power = data[statsindex - 22]
                                                money = data[statsindex - 21]
                                                red_money = data[statsindex - 20]
                                                tickets = data[statsindex - 19]
                                                cloaks = data[statsindex - 18]
                                                fragments_of_d2 = data[statsindex - 17]
                                                fragments_of_ktn = data[statsindex - 16]
                                                ancient_d2 = data[statsindex - 15]
                                                attempts = data[statsindex - 14]
                                                hp = data[statsindex - 13]
                                                min_dmg = data[statsindex - 12]
                                                max_dmg = data[statsindex - 11]
                                                crit_ch = data[statsindex - 10]
                                                crit_dmg = data[statsindex - 9]
                                                evade = data[statsindex - 8]
                                                l_kn = data[statsindex - 7]
                                                l_arm = data[statsindex - 6]
                                                l_mask = data[statsindex - 5]
                                                l_cloak = data[statsindex - 4]
                                                l_ktn = data[statsindex - 3]
                                                luck = data[statsindex - 2]
                                                user_id = data[statsindex - 1]
                                        print('Logging in is successful')
                                        print("Welcome " + str(username) + '!')
                                    else:
                                        print('Incorrect password')
                                else:
                                    print('Incorrect password')
                            else:
                                print('Incorrect password')
                        else:
                            print('Incorrect format')
                    else:
                        print('Incorrect login')
                else:
                    print('Incorrect login')
            else:
                print('Incorrect format')
        else:
            print('Login or register before you play!')
            print('/log to login')
            print('/reg to register')

