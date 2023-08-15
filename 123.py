
l_kn = 8
enemy_name = ["Fly", "Cockroach", "Frog", "Spider", "Snake", "Puppy", "Goat", "Black Panda"]
enemy_hp = [10, 50, 200, 400, 2000, 5000, 8000, 25000]
enemy_dmg = [2, 7, 15, 50, 200, 700, 1100, 3000]
money_gain_mim = [20, 40, 70, 130, 300, 444, 700, 1000]
money_gain_max = [30, 65, 120, 200, 450, 777, 1500, 5000]
power_rcmd = [1, 10, 32, 70, 300, 900, 1300, 2000]


money = 1
print(cost[l_kn])
if money >= cost[l_kn]:
    print("Upgrade to level " + str(l_kn + 1) + "?")
    print("Cost is " + str(cost))
    print("Success chance is " + str(chance) + "%")
    askin = input("Type yes or no:")
    if "y" in askin:
        money -= cost
        print('Enchanting! 3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)
        x = random.randint(1, y)
        if x <= rch:
            y = 1000
            min_dmg += 550
            max_dmg += 590
            l_kn += 1
            power += 450
            print("Upgraded! Knife is level " + str(l_kn))
            print("Your DMG is " + str(min_dmg) + "-" + str(max_dmg))
        else:
            y -= 110
            print("Fail... Your weapon's level is still " + str(l_kn))
        print('Wanna try one more time?')
    else:
        print("Returning back")
else:
    print("Not enough money!")