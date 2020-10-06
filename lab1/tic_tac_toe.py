# Tic Tac Toe

import random




def insert(board,letter, pos):
    board[pos] = letter


def spaceisfree(board,pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or                # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or                        # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or                        # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or                        # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or                        # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or                        # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or                        # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le))                          # diagonal


def playerMove():
    run = True
    while run:
        move = int(input('Chose a position from 1-9'))
        if move > 0 and move < 10:
            if spaceisfree(board,move):
                run = False
                insert(board,'X', move)
            else:
                print('Sorry, this position is already occupied!')
        else:
            print('Wrong Input!! Choose a position from 1-9')
       


def compMove():
    # Given a board and the computer's letter, determine where to move and return that move.
    computer = 'O'
    player = 'X'
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = board[:]
        if spaceisfree(copy, i):
            insert(copy, computer, i)
            if isWinner(copy, computer):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = board[:]
        if spaceisfree(copy, i):
            insert(copy, player, i)
            if isWinner(copy, player):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if spaceisfree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def chooseRandomMoveFromList(board, movesList):
    
    possibleMoves = []
    for i in movesList:
        if spaceisfree(board, i):
            possibleMoves.append(i)
            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    board = [' ' for x in range(10)]
    print('****************************')
    print('Let\'s start the game Tic Tac Toe \n You are X in this game')
    
    printBoard(board)
    flag = 0

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('The computer has beaten you! You lose.')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if isBoardFull(board) and flag==0:
                print('The game is a tie!')
                break
            else:
                insert(board,'O', move)
                print('Computer placed \'O\' at position : ', move)
                printBoard(board)
        else:
            print('The Player has won the game!')
            break

    

main()
while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        main()
    else:
        break
