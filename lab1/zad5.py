"""
while True:


    if  break

"""
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def printBoard():
    print('    A   B   C')
    for i in range(3):
        print('  -------------')
        print(f'{i+1} | {board[i][0]} | {board[i][1]} | {board[i][2]} |')
    print('  -------------')

def currentTurn():
    countX = 0
    countY = 0
    for row in board:
        for item in row:
            if item == 'X':
                countX += 1
            elif item == 'O':
                countY += 1
    if countX <= countY:
        # print('X\'s move')
        return 'X'
    # print('O\'s move')
    return 'O'

def move(row, column):
    marker = currentTurn()
    row = int(row)
    row -= 1
    column = column.upper()
    if 1 != [0, 1, 2].count(row):
        print('Incorrect row number!')
        return False
    if column == 'A':
        column = 0
    elif column == 'B':
        column = 1
    elif column == 'C':
        column = 2
    else:
        print('Incorrect column!')
        return False
    board[row][column] = marker

def isListEqual(list):
    if list.count(list[0]) == len(list) and list[0] != ' ':
        return True
    return False


def isGameOver():
    diagonalDown = []
    diagonalUp = []
    for i in range(3):
        vertical = []
        if isListEqual(board[i]):
            return True
        for j in range(3):
            vertical.append(board[j][i])
            if (i == j):
                diagonalDown.append(board[i][j])
            if (i + j == 2):
                diagonalUp.append(board[i][j])
        if isListEqual(vertical):
            return True
    if isListEqual(diagonalDown) or isListEqual(diagonalUp):
        return True
    return False


def isTie():
    """checks if game ended with a tie"""
    countEmptySquares = 0
    for row in board:
        for item in row:
            if item == ' ':
                countEmptySquares += 1
    if countEmptySquares == 0:
        return True
    return False


def readMove():
    while True:
        column = input('Enter a letter to choose column A-C: ')
        row = input('Enter a number to choose row 1-3: ')
        move(row, column)
        printBoard()
        if isGameOver():
            print(f'Player ({currentTurn()}) won')
            break
        if isTie():
            print('It\'s tie!')
            break
        print(f'{currentTurn()}\'s move')

print(f'{currentTurn()}\'s move')
printBoard()
readMove()