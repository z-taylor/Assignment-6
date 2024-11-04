# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment6B.py
import random
flag = True
while flag:
    try:
        width = input("Please enter how wide you want the board to be: ")
        height = input("Please enter how tall you want the board to be: ")
        if int(height)<=0 or int(width)<=0:
            raise ValueError
        flag = False
        width, height = int(width), int(height)
    except:
        print(f"You entered {width} for the width and {height} for the height. One or both of these is invalid. Please try again.")

board = []
secretBoard = []
numTreasures = 0
for i in range(height):
    board.append([])
    secretBoard.append([])
    tempList = []
    showList = []
    for n in range(width):
        treasureChance = random.randint(0, 10)
        tempList.append("T" if treasureChance >= 7 else "O")
        numTreasures += 1 if treasureChance >= 7 else 0
        showList.append("O")
    board[i] = showList
    secretBoard[i] = tempList
for i in range(len(board)):
    print(board[i])
print(f"There are {numTreasures} treasures hidden on the board. Can you find them all?")

flag = True
while flag:
    flag1 = True
    try:
        collumnNum = input(f"Enter the collumn number where you think the treasure is (1-{width}): ")
        rowNum = input(f"Enter the row number where you think the treasure is (1-{height}): ")
        if not (1 <= int(rowNum) <= height and 1 <= int(collumnNum) <= width):
            raise ValueError
        flag1 = False
        rowNum, collumnNum = int(rowNum)-1, int(collumnNum)-1
    except:
        print(f"You entered {rowNum} for the row and {collumnNum} for the collumn. One or both of these is invalid. Please try again.")
        continue
    if secretBoard[rowNum][collumnNum]=="T":
        board[rowNum][collumnNum] = "X"
        numTreasures -= 1
        print(f"Congratulations! You found a treasure! There are {numTreasures} left.")
    else:
        print(f"There is no treasure at ({collumnNum+1}, {rowNum+1})")
    flag = False if numTreasures==0 else True
print("You win!")
for i in range(len(board)):
    print(board[i])