import sys
import pdb
import random
from itertools import permutations
if __name__ == '__main__':
    pathDir = "../../utils"
    sys.path.insert(0,pathDir)
from permute import *
from stopwatch import *

def getRandom(n):
    return int(random.random() * n)

def getRandomPos(n):
    bp = getRandom(n*n)
    rowP = bp % n
    colP = int(bp / n)
    return (rowP,colP)

def score(board):
    n = len(board)
    conflictsList = []
    for i in range(n):
        pos = board[i]
        row = pos[0]
        col = pos[1]
        conflicts = 0
        for y in range(n):
            # score i against all other pieces
            if y == i:
                continue
            pos_y = board[y]
            row_y = pos_y[0]
            col_y = pos_y[1]
            if row == row_y:
                #DEBUG("ROW CONFLICT: {0} {1}".format(i,y))
                conflicts += 1
            elif col == col_y:
                #DEBUG("COL CONFLICT: {0} {1}".format(i,y))
                conflicts += 1
            elif (row-col) == (row_y-col_y):
                #DEBUG("DIAG CONFLICT -ve: {0} {1}".format(i,y))
                conflicts += 1
            elif (row+col) == (row_y+col_y):
                #DEBUG("DIAG CONFLICT +ve: {0} {1}".format(i,y))
                conflicts += 1
        conflictsList  += [conflicts]
    return conflictsList



def getInitialBoard(n):
    """Get an initial set of board positions for n queens. i.e. an nxn board.
    We represent the board as a vector of tuples (row,col).
    Each tuple represent the position of a queen on the board.
    """
    offset = getRandom(64)
    maxPos = n*n
    board = []
    for i in range(n):
        rowP = offset % n
        colP = int(offset / n)
        board = board + [(rowP,colP)]
        #if offset == 0:
        #    offset = getRandom(64)
        #offset = (offset * 2) % maxPos
        offset = getRandom(64)
    return board

def getPositionToImprove(scoreCard):
    n = len(scoreCard)
    # Get any randon position with conflicts to improve on
    pos = getRandom(n)
    while scoreCard[pos] == 0:
        pos = (pos + 1) % n
    return pos

def totalScores(scoreCard):
    tot = 0
    for i in scoreCard:
        tot += i
    return tot

def improveBoard(board, scoreCard, pos):
    n = len(board)
    total = totalScores(scoreCard)
    posRowCol = board[pos]
    minScore = total-1 # This forces us to always make a change whether it imroves overall score or not
    minList = []
    # find a new position that minimises total board score
    for newPos in range(n*n):
        rowP = newPos % n
        colP = int(newPos / n)
        if posRowCol == (rowP, colP):
            #ignore
            continue
        else:
            # change position and score
            board[pos] = (rowP,colP)
            newTotal = totalScores(score(board))
            # record minimm scores
            if newTotal < minScore:
                minList = [(rowP,colP)]
            elif newTotal == minScore:
                minList += [(rowP,colP)]
    
    mLen = len(minList)
    if mLen == 0:
        # if we can not improve make a random change.
        # This make it work. Without it it was getting stuck a lot. With this in it very seldom gets stuck
        board[pos] = getRandomPos(n)
        return
    elif mLen > 1:
        z = getRandom(mLen)
        board[pos] = minList[z]
    else:
        assert mLen==1
        board[pos] = minList[0]
    #DEBUG("REPOSITION: {0} {1} - old score {2}, new score {3}".format(posRowCol, board[pos], total, newTotal ))


def feedback(numIters):
    if numIters % 200 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
    if numIters % 1000 == 0:
        sys.stdout.write('\n')
        sys.stdout.flush()

def iteractiveRepair(board):
    n = len(board)
    MAXITERS = 9999
    numIters = 1
    #DEBUG("BOARD: {0}".format(board))
    scoreCard = score(board)
    total = totalScores(scoreCard)
    while (total > 0) and (numIters < MAXITERS):
        #DEBUG("Iteration [{0}]: score={1}".format(numIters, total))
        pos = getPositionToImprove(scoreCard)
        improveBoard(board, scoreCard, pos)
        scoreCard = score(board)
        #DEBUG("BOARD: {0}".format(board))
        #DEBUG("Scores: {0}".format(scoreCard))
        total = totalScores(scoreCard)
        numIters += 1
        feedback(numIters)
    if total == 0:
        print ("Solution found in {0} iterations:".format(numIters))
        print("BOARD: {0}".format(board))
    else:
        print("Failed to find a solution")

def main():
    SW = STOPWATCH()
    SW.start()
    #pdb.set_trace()
    board = getInitialBoard(8)
    #board = [(6, 6), (5, 5), (7, 5), (6, 6), (4, 7), (1, 1), (1, 5), (5, 1)]
    iteractiveRepair(board)
    SW.stopAndPrint()

if __name__ == '__main__':
    main()