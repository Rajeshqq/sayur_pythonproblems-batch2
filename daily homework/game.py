import random

game = ["rock", "paper", "scissors"]
bot = random.choice(game)
count=0

print("1. Rock")
print("2. Paper")
print("3. Scissors")
while(True):
    bot = random.choice(game)
    userinput = int(input("Enter your choice 1,2,3,4: "))

    if userinput == 1:
        user = "rock"
    elif userinput == 2:
        user = "paper"
    elif userinput == 3:
        user = "scissors"
    elif userinput==4:
        break

    print("You chose:", user)
    print("Bot chose:", bot)

    if user == bot:
        print("It's a tie!")
    elif (user == "rock" and bot == "scissors"):  
        print("You win!")
        count+=1
    elif(user=="paper"and bot=="rock"):
        print("you win!")
        count+=1
    elif(user=="scissors"and bot=="paper"):
        print("you win!")
        count+=1
    else:
        print("You lose!")
print("[points count : ",count)