import os
import sys
import subprocess as sp

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

player = ['O', 'X']
turnCount = 0
gameOver = False

# print screan and draw board with what character is stored in each array board[row][col]
def drawBoard():
    x=sp.call('cls',shell=True)
    print(" %c | %c | %c " % (board[0][0],board[0][1],board[0][2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[1][0],board[1][1],board[1][2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[2][0],board[2][1],board[2][2]))    
    print("   |   |   ")    


def checkWin():
    # checks all rows and cols for winning board arrangement
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] != " " or board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    # checks if diagonals have winning board arrangement
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

# convert position 1-9 to the [row][col] format
def getPos(num):
    if num < 4:
        row = 0
    elif num < 7:
        row = 1
    elif num < 10:
        row = 2
    if not (num % 3) == 0:
        col = (num % 3) - 1
    else:
        col = 2
    return row, col

# check who's turn it is by checking the amount of turns
def whosTurn():
    if (turnCount % 2) == 0:
        return 0
    else:
        return 1


def runTurn():
    # upkeep the turn count and set whos turn it is
    global turnCount
    turnCount += 1
    global playerTurn
    playerTurn = whosTurn()
    # getting player input
    try:
        position = int(input("Choose your position (1-9): ").strip())
        position = getPos(position)
        if not board[position[0]][position[1]] == ' ':
            print("Please chose a tile not taken!")
            turnCount -=1
            return runTurn()
        board[position[0]][position[1]] = player[playerTurn]
    except IndexError as e:
        print("Please enter valid position!")
        print(e)
        turnCount -=1
        return runTurn()
    except ValueError as e:
        print("Please enter valid position!")
        print(e)
        turnCount -=1
        return runTurn()
    

def restart():
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        os.execv(sys.executable, ['python'] + sys.argv)


def playAgain():
    check = str(input("Would you like to play again? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return playAgain()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return playAgain


def playGame():
    # run 9 turns and check if anybody won each turn
    while turnCount < 9:
        drawBoard()
        runTurn()
        drawBoard()
        if checkWin():
            print(player[playerTurn] + ' Won!!')
            break
    if not checkWin():
        print("Game is a tie!")
        
# main game loop abstracted
playGame()
if playAgain():
    restart()

