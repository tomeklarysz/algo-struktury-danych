import random
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
        return 'X'
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
    if board[row][column] == ' ':
        board[row][column] = marker
    else:
        print('This square is already taken!')

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
    computer = isPlayingAgainstBot()
    while True:
        if computer and currentTurn() == 'O':
            computerMove()
            printBoard()
            if isGameOver():
                print('Player (O) won')
                break
            if isTie():
                print('It\'s tie!')
                break
            print(f'{currentTurn()}\'s move')
            continue
        column = input('Enter a letter to choose column A-C: ')
        row = input('Enter a number to choose row 1-3: ')
        move(row, column)
        printBoard()
        if isGameOver():
            print('Player (X) won')
            break
        if isTie():
            print('It\'s tie!')
            break
        print(f'{currentTurn()}\'s move')

def computerMove():
    diagonalDown = []
    diagonalUp = []
    emptySquares = []
    """bestOption[0] is optimal row, bestOption[1] is optimal column"""
    bestOption = [1, 1]
    for i in range(3):
        vertical = []
        if board[i].count('O') == 2 and board[i].count('X') == 0:
            """check if any row has 2 Os and is close to winning"""
            bestOption[0] = i
            bestOption[1] = board[i].index(' ')
            board[bestOption[0]][bestOption[1]] = 'O'
            return True
        if board[i].count('X') == 2 and board[i].count('O') == 0:
            """check if any row has 2 Xs and is close to winning"""
            bestOption[0] = i
            bestOption[1] = board[i].index(' ')
            board[bestOption[0]][bestOption[1]] = 'O'
            return True
        for j in range(3):
            vertical.append(board[j][i])
            if (i == j):
                diagonalDown.append(board[i][j])
            if (i + j == 2):
                diagonalUp.append(board[i][j])
            if board[i][j] == ' ':
                emptySquares.append([i, j])
        if vertical.count('O') == 2 and vertical.count('X') == 0:
            """if any column has 2 Xs and is close to winning"""
            bestOption[0] = vertical.index(' ')
            bestOption[1] = i
            board[bestOption[0]][bestOption[1]] = 'O'
            return True
        if vertical.count('X') == 2 and vertical.count('O') == 0:
            """if any column has 2 Xs and is close to winning"""
            bestOption[0] = vertical.index(' ')
            bestOption[1] = i
            board[bestOption[0]][bestOption[1]] = 'O'
            return True
    if diagonalDown.count('O') == 2 and diagonalDown.count('X') == 0:
        if diagonalDown.index(' ') == 0:
            bestOption[0] = 0
            bestOption[1] = 0
        elif diagonalDown.index(' ') == 1:
            bestOption[0] = 1
            bestOption[1] = 1
        else:
            bestOption[0] = 2
            bestOption[1] = 2
        board[bestOption[0]][bestOption[1]] = 'O'
        return True
    if diagonalDown.count('X') == 2 and diagonalDown.count('O') == 0:
        if diagonalDown.index(' ') == 0:
            bestOption[0] = 0
            bestOption[1] = 0
        elif diagonalDown.index(' ') == 1:
            bestOption[0] = 1
            bestOption[1] = 1
        else:
            bestOption[0] = 2
            bestOption[1] = 2
        board[bestOption[0]][bestOption[1]] = 'O'
        return True
    if diagonalUp.count('O') == 2 and diagonalUp.count('X') == 0:
        if diagonalUp.index(' ') == 0:
            bestOption[0] = 0
            bestOption[1] = 2
        elif diagonalDown.index(' ') == 1:
            bestOption[0] = 1
            bestOption[1] = 1
        else:
            bestOption[0] = 2
            bestOption[1] = 0
        board[bestOption[0]][bestOption[1]] = 'O'
        return True
    if diagonalUp.count('X') == 2 and diagonalUp.count('O') == 0:
        if diagonalUp.index(' ') == 0:
            bestOption[0] = 0
            bestOption[1] = 2
        elif diagonalDown.index(' ') == 1:
            bestOption[0] = 1
            bestOption[1] = 1
        else:
            bestOption[0] = 2
            bestOption[1] = 0
        board[bestOption[0]][bestOption[1]] = 'O'
        return True
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return False
    # pick random in case of no optimal
    draw = random.choice(emptySquares)
    board[draw[0]][draw[1]] = 'O'
    return False
    
def isPlayingAgainstBot():
    question = input('Do you want to play against computer? Y/N ')
    if question.upper() == 'Y':
        print('Playing against computer')
        return True
    elif question.upper() == 'N':
        print('Playing 2-player mode')
        return False
    print('Incorrect input')
    return isPlayingAgainstBot()

print(f'{currentTurn()}\'s move')
printBoard()
readMove()