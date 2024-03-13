import random

points1 = 0
points2 = 0
totaldicerolled = 0
dicerolledbyp1=0
dicerolledbyp2=0

def dice():
    return random.randint(1, 6)

def gamepoints(bot):
    if bot == 1:
        return 1
    elif bot == 2:
        return 5
    elif bot == 3:
        return 15
    elif bot == 4:
        return -15
    elif bot == 5:
        return -5
    elif bot == 6:
        return -1

count = 0

while True:
    count += 1

    if count % 2 != 0:
        print("Player 1")
        
        bot = dice()
        points1 += gamepoints(bot)
        totaldicerolled += 1
        dicerolledbyp1+=1
    else:
        print("Player 2")  
        
        bot = dice()
        points2 += gamepoints(bot)
        totaldicerolled += 1
        dicerolledbyp2+=1
    
    print("Player 1 points:", points1, "Dice rolled:", dicerolledbyp1)
    print("Player 2 points:", points2, "Dice rolled:", dicerolledbyp2)

    if points1 >= 200 or points2 >= 200:
        break

print("Game over!")
print("total dice rolled", totaldicerolled)
if points1 > points2:
    print("Player 1 wins!")
elif points2 > points1:
    print("Player 2 wins!")
else:
    print("It's a tie!")
