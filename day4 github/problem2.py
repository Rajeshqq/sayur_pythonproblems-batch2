import random

board = [['*','*','*','*','*','*'],['*','*','*','*','*','*'],['*','*','*','*','*','*'],
         ['*','*','*','*','*','*'],['*','*','*','*','*','*'],['*','*','*','*','*','*']]
pointsofA = 0
pointsofB = 0


def boardFun():
    for game in board:
        for star in game:
            print(star, end="   ")
        print(" ")
        print(" ")


def dicefun():
    diceno = random.randint(1, 6)
    return diceno


def gamefun():
    global pointsofA
    global pointsofB

    player1 = input("Enter the player 1 name: ")
    player2 = input("Enter the player 2 name: ")

    while True:
        print("Player:", player1)
        print("Roll the dice: Type 1 to roll the dice")

        getrow = int(input("Press 1 to get the row: "))
        if getrow == 1:
            row = dicefun()
            print("Row:", row)

        getcolumn = int(input("Press 2 to get the column: "))
        if getcolumn == 2:
            column = dicefun()
            print("Column:", column)

        if board[row - 1][column - 1] == "*":
            board[row - 1][column - 1] = "A"
        else:
            pointsofA+= 1
            board[row - 1][column - 1] = "A"

        boardFun()
        print(f"Point of {player1}: {pointsofA}")
        print(f"Point of {player2}: {pointsofB}")

        print("Player:", player2)
        print("Roll the dice: Type 1 to roll the dice")

        getrow = int(input("Press 1 to get the row: "))
        if getrow == 1:
            row = dicefun()
            print("Row:", row)

        getcolumn = int(input("Press 2 to get the column: "))
        if getcolumn == 2:
            column = dicefun()
            print("Column:", column)

        if board[row - 1][column - 1] == "*":
            board[row - 1][column - 1] = "B"
        else:
            pointsofB += 1
            board[row - 1][column - 1] = "B"

        boardFun()
        print(f"Point of {player2}: {pointsofB}")
        print(f"Point of {player1}: {pointsofA}")

        if pointsofA >= 5:
            print(f"{player1} is the winner!")
            break
        elif pointsofB >= 5:
            print(f"{player2} is the winner!")
            break


gamefun()