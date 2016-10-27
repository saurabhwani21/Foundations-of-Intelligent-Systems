"""
filename: tttAB.py
Author: Saurabh A. Wani

"""
import sys


def displayBoard(table):
    """
        Displays the board on console.
        :param table: The list containing all the value.
        :return: None
        """
    for x in range(len(table)):
        if x%3 == 0:
            print()
        print(table[x],end="")
        if (x not in (2,5,8)):
            print("|",end="")
    print()

def takeInput(table):
    """
    Take input from the user.
    :param table: The list containing the values on the board.
    :return: None
    """
    print("User's turn.")
    loc = int(input("Enter the location."))
    c = 0
    while c<5:
        if loc in availableMoves(table):
            table[loc] = "X"
            displayBoard(table)
            print("AI's turn.")
            return
        else:
            loc = int(input("Try again."))
            c += 1
    print("Sorry you ran out of turns!")
    sys.exit(0)




def checkWin(table):
    """
        Checks if the anyone has won.
        :param table: The list containing the values on the board.
        :return: Winner game piece if anyone has won else None
    """

    #checking for rows
    for x in range(0,7,3):
        if table[x] == table[x+1] == table[x+2]:
            if table[x] is not " ":
                return table[x]

    for y in range(0,3,1):
        if table[y] == table[y + 3] == table[y + 6]:
            if table[y] is not " ":
                return table[y]

    if table[0] == table[4] == table[8]:
        if table[0] is not " ":
            return table[0]

    if table[2] == table[4] == table[6]:
        if table[2] is not " ":
            return table[2]

def checkTie(table):
    """
        Check if the game has been tied.
        :param table: The list containing the values on the board.
        :return: True if it is, else false if it has not been tied.
    """
    if " " in table:
        return False
    else:
        return True

def availableMoves(table):
    """
        Check the empty spots on the game board.
        :param table: The list containing the values on the board.
        :return: List of available moves.
    """
    counter = 0
    availableM = []
    for x in table:
        if x == " ":
            availableM.append(counter)
        counter += 1
    return availableM

def miniMax(table, gamePiece, counter):
    """
        Gives the location where the AI's pieces will be inserted.
        :param table: The list containing the game pieces.
        :param gamePiece: User's game piece.
        :param counter: Variable to keep track of number of states.
        :return: Output value obtained from maxAI().
    """
    return maxVal(table, gamePiece, -1000, 1000, counter)


def maxVal(table, gamePiece, alpha, beta, counter):
    """
        Calculates the best possible position for the AI to win.
        :param table: The list containing the game pieces.
        :param gamePiece: Piece used in the game.
        :param counter: Variable to keep track of number of states.
        :param alpha: Value used to compare.
        :param beta: Value used to compare.
        :return: Besr value, location of game piece and the counter.
        """
    result = []
    value = -1000


    cWin = checkWin(table)
    if cWin is not None:
        if cWin == "X":
            return -1, -1, counter
        else:
            return 1, -1, counter

    # check if board is full
    if checkTie(table):
        return 0,-1, counter

    movesList = availableMoves(table)


    for x in movesList:
        counter+= 1
        table[x] = gamePiece
        res,move, counter = minVal(table, 'X', alpha, beta, counter)
        table[x] = " "
        if value < res:
            value = res
        if value >= beta:
            return value, x, counter
        alpha = max(alpha, value)
        result.append(res)
    return value, movesList[result.index(value)], counter

def minVal(table, gamePiece, alpha, beta, counter):
    """
        Calculates the best possible position for the AI to win.
        :param table: The list containing the game pieces.
        :param gamePiece: Piece used in the game.
        :param counter: Variable to keep track of number of states.
        :param alpha: Value used to compare.
        :param beta: Value used to compare.
        :return: Besr value, location of game piece and the counter.
    """
    result = []
    value = 1000

    cWin = checkWin(table)
    if cWin is not None:
        if cWin == "X":
            return -1, -1, counter
        else:
            return 1, -1, counter

    # check if board is full
    if checkTie(table):
        return 0, -1, counter

    movesList = availableMoves(table)

    for x in movesList:
        table[x] = gamePiece
        res, move, counter= maxVal(table, 'O', alpha, beta, counter)
        table[x] = " "
        if value > res:
            value = res
        if value <= alpha:
            return value, x, counter
        beta = min(beta, value)
        result.append(res)
    return value, movesList[result.index(value)], counter


def main():
    # To continue the game.
    flag = None

    #To keep track of number of states.
    counter = 0

    while (flag != "exit"):
        print("Let's start!")
        table = [" "," "," "," "," "," "," "," "," "]

        displayBoard(table)

        # taking first input from user
        takeInput(table)
        c = 1

        while (len(availableMoves(table))) != 0:
            if c == 1:
                value, location, counter = miniMax(table, "O", counter)
                print("counter= ", counter)
                table[location] = "O"
                displayBoard(table)
                c = 0
            else:
                takeInput(table)
                displayBoard(table)
                c = 1
            decision = checkWin(table)
            if decision is "X":
                print("Human wins!")
                break
            elif decision is "O":
                print("AI wins!")
                break
            elif checkTie(table):
                print("Its a tie!")
                break
        flag = input("Type 'exit' to terminate or hit enter to continue.")


if __name__ == '__main__':
    main()
