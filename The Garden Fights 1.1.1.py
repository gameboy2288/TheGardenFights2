import random
import time

print("Hello! That's my first easy-made rpg!")
print("/check to check out your stats")
print("/kn or /arm to inscrease your power")
print("/g (level number) to fight")
print("Max knife 10 | Max armor 9 | Max level 5")

lvl = 0
power = 1
money = 9999
attempts = 0
hp = 20
dmg = 3
l_kn = 1
l_arm = 1

while True:
    command = input()
    if '/check' in command:
        print(str(lvl) + " levels passed")
        print(str(power) + " power")
        print(str(money) + " money")
        print(str(attempts) + " attempts")
        print(str(hp) + " HP")
        print(str(dmg) + " DMG")
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
    elif "/kn" in command:
        if dmg == 3:
            if money >= 5:
                money -= 5
                dmg += 2
                l_kn += 1
                power += 1
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 5:
            if money >= 10:
                money -= 10
                dmg += 3
                l_kn += 1
                power += 2
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 8:
            if money >= 20:
                money -= 20
                dmg += 4
                l_kn += 1
                power += 3
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 12:
            if money >= 50:
                money -= 50
                dmg += 7
                l_kn += 1
                power += 5
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 19:
            if money >= 100:
                money -= 100
                dmg += 13
                l_kn += 1
                power += 7
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 32:
            if money >= 200:
                money -= 200
                dmg += 25
                l_kn += 1
                power += 12
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 57:
            if money >= 400:
                money -= 400
                dmg += 47
                l_kn += 1
                power += 19
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 104:
            if money >= 1000:
                money -= 1000
                dmg += 110
                l_kn += 1
                power += 35
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        elif dmg == 214:
            if money >= 2000:
                money -= 2000
                dmg += 180
                l_kn += 1
                power += 71
                print("Upgraded! Knife is level " + str(l_kn))
                print("Your DMG is " + str(dmg))
            else:
                print("Not enough money!")
        else:
            print("Your DMG is maximum!")
    elif "/arm" in command:
        if hp == 20:
            if money >= 5:
                money -= 5
                hp += 5
                l_arm += 1
                power += 1
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        elif hp == 25:
            if money >= 10:
                money -= 10
                hp += 8
                l_arm += 1
                power += 2
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        elif hp == 33:
            if money >= 20:
                money -= 20
                hp += 12
                l_arm += 1
                power += 3
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        elif hp == 45:
            if money >= 50:
                money -= 50
                hp += 25
                l_arm += 1
                power += 5
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        elif hp == 70:
            if money >= 100:
                money -= 100
                hp += 60
                l_arm += 1
                power += 13
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        elif hp == 130:
            if money >= 200:
                money -= 200
                hp += 130
                l_arm += 1
                power += 21
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        elif hp == 260:
            if money >= 500:
                money -= 500
                hp += 300
                l_arm += 1
                power += 35
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        elif hp == 560:
            if money >= 1212:
                money -= 1212
                hp += 666
                l_arm += 1
                power += 66
                print("Upgraded! Armor is level " + str(l_arm))
                print("Your HP is " + str(hp))
            else:
                print("Not enough money!")
        else:
            print("Your HP is maximum!")
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
                    fly_hp = fly_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(fly_hp) + "/10")
                    time.sleep(1.3)
                    your_hp = your_hp - fly_dmg
                    print("Fly's biting you with " + str(fly_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if fly_hp <= 0:
                    if lvl == 0:
                        lvl += 1
                    money += 4
                    print("You won and got 4 money!")
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
                    cockroach_hp = cockroach_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(cockroach_hp) + "/50")
                    time.sleep(1.3)
                    your_hp = your_hp - cockroach_dmg
                    print("Cockroach's biting you with " + str(cockroach_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if cockroach_hp <= 0:
                    if lvl == 1:
                        lvl += 1
                    money += 12
                    attempts += 1
                    print("You won and got 12 money!")
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
                    frog_hp = frog_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(frog_hp) + "/200")
                    time.sleep(1.3)
                    your_hp = your_hp - frog_dmg
                    print("Frog's biting you with " + str(frog_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if frog_hp <= 0:
                    if lvl == 2:
                        lvl += 1
                    money += 35
                    attempts += 1
                    print("You won and got 35 money!")
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
                    spider_hp = spider_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(spider_hp) + "/400")
                    time.sleep(1.3)
                    your_hp = your_hp - spider_dmg
                    print("Spider's biting you with " + str(spider_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if spider_hp <= 0:
                    if lvl == 3:
                        lvl += 1
                    money += 100
                    attempts += 1
                    print("You won and got 100 money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
        if '/g 5' in command:
            if lvl >= 0:
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
                    snake_hp = snake_hp - dmg
                    print("You're hitting with " + str(dmg) + " DMG! " + str(snake_hp) + "/2000")
                    time.sleep(1.3)
                    your_hp = your_hp - snake_dmg
                    print("Snake's biting you with " + str(snake_dmg) + " DMG! " + str(your_hp) + "/" + str(hp))
                    time.sleep(1.3)
                if snake_hp <= 0:
                    if lvl == 4:
                        lvl += 1
                    money += 333
                    attempts += 1
                    print("You won and got 333 money!")
                else:
                    print("You lost!")
            else:
                print("First pass previeous levels!")
    else:
        print('Wrong command!')
