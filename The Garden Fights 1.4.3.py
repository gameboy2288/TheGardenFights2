import random
import time
import json

print("Hello! That's my first easy-made rpg!")
print("/check to check out your stats")
print("/kn or /arm to inscrease your power")
print("/g (level number) to fight")
print("/save to save and /load to load")
print("Max knife 10 | Max armor 9 | Max mask 5 | Max level 5")

lvl = 0
power = 1
money = 13
attempts = 0
hp = 20
min_dmg = 3
max_dmg = 4
crit_ch = 0
crit_dmg = 0
l_kn = 1
l_arm = 1
l_mask = 0
tes = 0

data = [lvl, power, money, attempts, hp, min_dmg, max_dmg, crit_ch, crit_dmg, l_kn, l_arm, l_mask, tes]

while True:
    command = input()
    if '/test' in command and tes == 0:
        tes += 1
        money += 200000
        print("You've gained 200 money")
    elif '/load' in command:
        with open('data.txt') as json_file:
            data = json.load(json_file)
            for ig in data:
                lvl = data[0]
                power = data[1]
                money = data[2]
                attempts = data[3]
                hp = data[4]
                min_dmg = data[5]
                max_dmg = data[6]
                crit_ch = data[7]
                crit_dmg = data[8]
                l_kn = data[9]
                l_arm = data[10]
                l_mask = data[11]
                tes = data[12]
        print("You've just loaded your progress!")
    elif '/save' in command:
        data = [lvl, power, money, attempts, hp, min_dmg, max_dmg, crit_ch, crit_dmg, l_kn, l_arm, l_mask, tes]
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
        print("You've just saved your progress!")
    elif '/check' in command:
        print(str(lvl) + " levels passed")
        print(str(power) + " power")
        print(str(money) + " money")
        print(str(attempts) + " attempts")
        print(str(hp) + " HP")
        print(str(min_dmg) + "-" + str(max_dmg) + " DMG")
        if l_mask >= 1:
            print(str(crit_ch) + " crit chance")
            print(str(crit_dmg) + " crit DMG")
        if l_kn == 1:
            print("5 money for Knife lvl 2!")
        elif l_kn == 2:
            print("10 money for Knife lvl 3!")
        elif l_kn == 3:
            print("20 money for Knife lvl 4!")
        elif l_kn == 4:
            print("50 money for Knife lvl 5!")
        elif l_kn == 5:
            print("100 money for Knife lvl 6!")
        elif l_kn == 6:
            print("200 money for Knife lvl 7!")
        elif l_kn == 7:
            print("400 money for Knife lvl 8!")
        elif l_kn == 8:
            print("1000 money for Knife lvl 9!")
        elif l_kn == 9:
            print("2000 money for Knife lvl 10!")
        elif l_kn == 10:
            print("Your Knife is on maximum!")
        if l_arm == 1:
            print("5 money for Armor lvl 2!")
        elif l_arm == 2:
            print("10 money for Armor lvl 3!")
        elif l_arm == 3:
            print("20 money for Armor lvl 4!")
        elif l_arm == 4:
            print("50 money for Armor lvl 5!")
        elif l_arm == 5:
            print("100 money for Armor lvl 6!")
        elif l_arm == 6:
            print("200 money for Armor lvl 7!")
        elif l_arm == 7:
            print("500 money for Armor lvl 8!")
        elif l_arm == 8:
            print("1212 money for Armor lvl 9!")
        elif l_arm == 9:
            print("Your Armor is on maximum!")
        if l_mask == 0:
            if l_kn <= 1:
                print("Enchance your knife to 7 level to buy a mask!")
            else:
                print("Buy a mask for 666 money!")
        elif l_mask == 1:
            print("2000 money for Mask lvl 2!")
        elif l_mask == 2:
            print("3000 money for Mask lvl 3!")
        elif l_mask == 3:
            print("4000 money for Mask lvl 4!")
        elif l_mask == 4:
            print("5000 money for Mask lvl 5!")
    elif "/kn" in command:
        if l_kn == 1:
            if money >= 5:
                money -= 5
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 90:
                    min_dmg += 2
                    max_dmg += 3
                    l_kn += 1
                    power += 1
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 2:
            if money >= 10:
                money -= 10
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 80:
                    min_dmg += 3
                    max_dmg += 4
                    l_kn += 1
                    power += 2
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 3:
            if money >= 20:
                money -= 20
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 73:
                    min_dmg += 4
                    max_dmg += 6
                    l_kn += 1
                    power += 3
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 4:
            if money >= 50:
                money -= 50
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 66:
                    min_dmg += 7
                    max_dmg += 9
                    l_kn += 1
                    power += 5
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 5:
            if money >= 100:
                money -= 100
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 59:
                    min_dmg += 13
                    max_dmg += 16
                    l_kn += 1
                    power += 7
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 6:
            if money >= 200:
                money -= 200
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 52:
                    min_dmg += 25
                    max_dmg += 35
                    l_kn += 1
                    power += 12
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 7:
            if money >= 400:
                money -= 400
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 46:
                    min_dmg += 47
                    max_dmg += 66
                    l_kn += 1
                    power += 19
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 8:
            if money >= 1000:
                money -= 1000
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1, 100)
                if x <= 42:
                    min_dmg += 110
                    max_dmg += 140
                    l_kn += 1
                    power += 35
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif l_kn == 9:
            if money >= 2000:
                money -= 2000
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 38:
                    min_dmg += 180
                    max_dmg += 228
                    l_kn += 1
                    power += 71
                    print("Upgraded! Knife is level " + str(l_kn))
                    print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
                else:
                    print("Fail... Your weapon's level is still " + str(l_kn))
            else:
                print("Not enough money!")
        else:
            print("Your DMG is maximum!")
    elif "/arm" in command:
        if hp == 20:
            if money >= 5:
                money -= 5
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 90:
                    hp += 5
                    l_arm += 1
                    power += 1
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif hp == 25:
            if money >= 10:
                money -= 10
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 80:
                    hp += 8
                    l_arm += 1
                    power += 2
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif hp == 33:
            if money >= 20:
                money -= 20
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 73:
                    hp += 12
                    l_arm += 1
                    power += 3
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif hp == 45:
            if money >= 50:
                money -= 50
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 66:
                    hp += 25
                    l_arm += 1
                    power += 5
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif hp == 70:
            if money >= 100:
                money -= 100
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 59:
                    hp += 60
                    l_arm += 1
                    power += 13
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif hp == 130:
            if money >= 200:
                money -= 200
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 52:
                    hp += 130
                    l_arm += 1
                    power += 21
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif hp == 260:
            if money >= 500:
                money -= 500
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 46:
                    hp += 300
                    l_arm += 1
                    power += 35
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
                print('Wanna try one more time?')
            else:
                print("Not enough money!")
        elif hp == 560:
            if money >= 1212:
                money -= 1212
                print('Enchanting! 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                x = random.randint(1,100)
                if x <= 41:
                    hp += 666
                    l_kn += 1
                    power += 66
                    print("Upgraded! Armor is level " + str(l_arm))
                    print("Your HP is " + str(hp))
                else:
                    print("Fail... Your weapon's level is still " + str(l_arm))
            else:
                print("Not enough money!")
        else:
            print("Your HP is maximum!")
    elif "/mask" in command:
        if l_kn >= 2:
            if l_mask == 0:
                if money >= 666:
                    money -= 666
                    x = random.randint(1,100)
                    if x <= 100:
                        crit_ch += 13
                        crit_dmg += 25
                        l_mask += 1
                        power += 30
                        print("You just bought a mask!")
                        print("Your crit chance is " + str(crit_ch))
                        print("Your crit damage is " + str(crit_dmg))
                    else:
                        print("Fail... Your mask's level is still " + str(l_arm))
                    print('Wanna upgrade it?')
                else:
                    print("Not enough money!")
            elif l_mask == 1:
                if money >= 2000:
                    money -= 2000
                    print('Enchanting! 3...')
                    time.sleep(1)
                    print('2...')
                    time.sleep(1)
                    print('1...')
                    time.sleep(1)
                    x = random.randint(1,100)
                    if x <= 13:
                        crit_ch += 2
                        crit_dmg += 15
                        l_mask += 1
                        power += 20
                        print("Upgraded! Mask is level " + str(l_mask))
                        print("Your crit chance is " + str(crit_ch))
                        print("Your crit damage is " + str(crit_dmg))
                    else:
                        print("Fail... Your mask's level is still " + str(l_mask))
                    print('Wanna try one more time?')
                else:
                    print("Not enough money!")
            elif l_mask == 2:
                if money >= 3000:
                    money -= 3000
                    print('Enchanting! 3...')
                    time.sleep(1)
                    print('2...')
                    time.sleep(1)
                    print('1...')
                    time.sleep(1)
                    x = random.randint(1,100)
                    if x <= 13:
                        crit_ch += 2
                        crit_dmg += 15
                        l_mask += 1
                        power += 20
                        print("Upgraded! Mask is level " + str(l_mask))
                        print("Your crit chance is " + str(crit_ch))
                        print("Your crit damage is " + str(crit_dmg))
                    else:
                        print("Fail... Your mask's level is still " + str(l_mask))
                    print('Wanna try one more time?')
                else:
                    print("Not enough money!")
            elif l_mask == 3:
                if money >= 4000:
                    money -= 4000
                    print('Enchanting! 3...')
                    time.sleep(1)
                    print('2...')
                    time.sleep(1)
                    print('1...')
                    time.sleep(1)
                    x = random.randint(1,100)
                    if x <= 13:
                        crit_ch += 2
                        crit_dmg += 15
                        l_mask += 1
                        power += 20
                        print("Upgraded! Mask is level " + str(l_mask))
                        print("Your crit chance is " + str(crit_ch))
                        print("Your crit damage is " + str(crit_dmg))
                    else:
                        print("Fail... Your mask's level is still " + str(l_mask))
                    print('Wanna try one more time?')
                else:
                    print("Not enough money!")
            elif l_mask == 4:
                if money >= 5000:
                    money -= 5000
                    print('Enchanting! 3...')
                    time.sleep(1)
                    print('2...')
                    time.sleep(1)
                    print('1...')
                    time.sleep(1)
                    x = random.randint(1,100)
                    if x <= 13:
                        crit_ch += 2
                        crit_dmg += 15
                        l_mask += 1
                        power += 20
                        print("Upgraded! Mask is level " + str(l_mask))
                        print("Your crit chance is " + str(crit_ch))
                        print("Your crit damage is " + str(crit_dmg))
                    else:
                        print("Fail... Your mask's level is still " + str(l_mask))
                    print('Wanna try one more time?')
                else:
                    print("Not enough money!")
            else:
                print("Your mask is on maximum!")
        else:
            print("You cannot buy mask until your knife is level 7!")
    elif '/g' in command:
        if '/g 1' in command:
            if lvl >= 0:
                print('Your opponent is a fly!')
                print('HP = 10/10')
                print('DMG = 2')
                time.sleep(1.6)
                attempts += 1
                your_hp = hp
                fly_hp = 10
                fly_dmg = 2
                while fly_hp >= 1 and your_hp >= 1:
                    dmg = random.randint(int(min_dmg), int(max_dmg))
                    crit = random.randint(1,100)
                    if crit <= crit_ch:
                        dmg += dmg * crit_dmg / 100
                        dmg = int(dmg)
                    fly_hp = fly_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(fly_hp) + "/10")
                    time.sleep(1.3)
                    your_hp = your_hp - fly_dmg
                    print("Fly's biting you with " + str(fly_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if fly_hp <= 0:
                    if lvl == 0:
                        lvl += 1
                    moneyg = 7
                    money += moneyg
                    print("You won and got " + str(moneyg) + " money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
        if '/g 2' in command:
            if lvl >= 1:
                print('Your opponent is a cockroach!')
                print('HP = 50/50')
                print('DMG = 7')
                print("Recomended power is 10")
                time.sleep(1.6)
                attempts += 1
                your_hp = hp
                cockroach_hp = 50
                cockroach_dmg = 7
                while cockroach_hp >= 1 and your_hp >= 1:
                    dmg = random.randint(int(min_dmg), int(max_dmg))
                    crit = random.randint(1,100)
                    if crit <= crit_ch:
                        dmg += dmg * crit_dmg / 100
                        dmg = int(dmg)
                    cockroach_hp = cockroach_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(cockroach_hp) + "/50")
                    time.sleep(1.3)
                    your_hp = your_hp - cockroach_dmg
                    print("Cockroach's biting you with " + str(cockroach_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if cockroach_hp <= 0:
                    if lvl == 1:
                        lvl += 1
                    moneyg = 35
                    money += moneyg
                    print("You won and got " + str(moneyg) + " money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
        if '/g 3' in command:
            if lvl >= 2:
                print('Your opponent is a frog!')
                print('HP = 200/200')
                print('DMG = 15')
                print("Recomended power is 32")
                time.sleep(1.6)
                attempts += 1
                your_hp = hp
                frog_hp = 200
                frog_dmg = 15
                while frog_hp >= 1 and your_hp >= 1:
                    dmg = random.randint(int(min_dmg), int(max_dmg))
                    crit = random.randint(1,100)
                    if crit <= crit_ch:
                        dmg += dmg * crit_dmg / 100
                        dmg = int(dmg)
                    frog_hp = frog_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(frog_hp) + "/200")
                    time.sleep(1.3)
                    your_hp = your_hp - frog_dmg
                    print("Frog's biting you with " + str(frog_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if frog_hp <= 0:
                    if lvl == 2:
                        lvl += 1
                    moneyg = 75
                    money += moneyg
                    print("You won and got " + str(moneyg) + " money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
        if '/g 4' in command:
            if lvl >= 3:
                print('Your opponent is a spider!')
                print('HP = 400/400')
                print('DMG = 50')
                print("Recomended power is 70")
                time.sleep(1.6)
                attempts += 1
                your_hp = hp
                spider_hp = 400
                spider_dmg = 50
                while spider_hp >= 1 and your_hp >= 1:
                    dmg = random.randint(int(min_dmg), int(max_dmg))
                    crit = random.randint(1,100)
                    if crit <= crit_ch:
                        dmg += dmg * crit_dmg / 100
                        dmg = int(dmg)
                    spider_hp = spider_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(spider_hp) + "/400")
                    time.sleep(1.3)
                    your_hp = your_hp - spider_dmg
                    print("Spider's biting you with " + str(spider_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if spider_hp <= 0:
                    if lvl == 3:
                        lvl += 1
                    moneyg = 200
                    money += moneyg
                    print("You won and got " + str(moneyg) + " money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
        if '/g 5' in command:
            if lvl >= 4:
                print('Your opponent is a snake!')
                print('HP = 2000/2000')
                print('DMG = 200')
                print("Recomended power is 300")
                time.sleep(1.6)
                attempts += 1
                your_hp = hp
                snake_hp = 2000
                snake_dmg = 200
                while snake_hp >= 1 and your_hp >= 1:
                    dmg = random.randint(int(min_dmg), int(max_dmg))
                    crit = random.randint(1,100)
                    if crit <= crit_ch:
                        dmg += dmg * crit_dmg / 100
                        dmg = int(dmg)
                    snake_hp = snake_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(snake_hp) + "/2000")
                    time.sleep(1.3)
                    your_hp = your_hp - snake_dmg
                    print("Snake's biting you with " + str(snake_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if snake_hp <= 0:
                    if lvl == 4:
                        lvl += 1
                    moneyg = 500
                    money += moneyg
                    print("You won and got " + str(moneyg) + " money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
        if '/g 6' in command:
            if lvl >= 5:
                print('Your opponent is a puppy!')
                print('HP = 5000/5000')
                print('DMG = 700')
                print("Recomended power is 700")
                time.sleep(1.6)
                attempts += 1
                your_hp = hp
                puppy_hp = 5000
                puppy_dmg = 700
                while puppy_hp >= 1 and your_hp >= 1:
                    dmg = random.randint(int(min_dmg), int(max_dmg))
                    crit = random.randint(1,100)
                    if crit <= crit_ch:
                        dmg += dmg * crit_dmg / 100
                        dmg = int(dmg)
                    puppy_hp = puppy_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(puppy_hp) + "/5000")
                    time.sleep(1.3)
                    your_hp = your_hp - puppy_dmg
                    print("Puppy's biting you with " + str(puppy_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if puppy_hp <= 0:
                    if lvl == 5:
                        lvl += 1
                    moneyg = 2000
                    money += moneyg
                    print("You won and got " + str(moneyg) + " money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
    else:
        print('Wrong command!')
