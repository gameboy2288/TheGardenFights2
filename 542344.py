import random

lvl = 0
x = 1
y = 10000
while True:
    if input():
        print(x, y)
        ch = random.randint(x, y)
        print(ch)
        if lvl == 0:
            if ch <= 1000:
                lvl += 1
                print("yes")
                x = 1
                y = 10000
            else:
                y -= 1000
        elif lvl == 1:
            if ch <= 1000:
                lvl += 1
                print("yes")
                x = 1
                y = 10000
            else:
                y -= 500
        elif lvl == 2:
            if ch <= 1000:
                lvl += 1
                print("yes")
                x = 1
                y = 10000
            else:
                y -= 250
        elif lvl == 3:
            if ch <= 1000:
                lvl += 1
                print("yes")
                x = 1
                y = 10000
            else:
                y -= 120