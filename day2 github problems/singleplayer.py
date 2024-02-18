#Its is a single player game where the user starts with 0 points. User keeps rolling the 
#dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 #added. If the number is odd, then if the number is 1,3 then the user has to jump. 
 # If the number is 5, then 3 points are added. The game ends when the user has 50 points.
import random
import sys

def dice(): 
    random_number = random.randint(0, 5)
    return random_number

points=0
while (True):
    roll = input("Do you want to roll the dice? (yes/no): ")
    if roll.lower() == "yes":
        result = dice()
        print("You rolled:", result)
        if result == 0:
            print("Game over. You rolled a 0.")
            break
        elif result%2==0:
            points+=2
            print(f"your point is {points}:")
        elif result==1 or result==3:
            points-=1
            print(f"your point is {points}:")
        elif result==5:
            points+=3
            print(f"your point is {points}:")
            
    elif roll.lower() == "no":
        print("Game ended by user.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    if(points==50):
        print("you won the game")
        break

print("Game end")
