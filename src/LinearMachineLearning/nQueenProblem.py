from array import *

"""
Algorithm -
 Regression model. Place queens sequentially and verify.

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# Created queenPosition with 4
queenPosition = [(-1,-1),(-1,-1),(-1,-1),(-1,-1)]
"""

board=[]
queenPosition=[[-1,-1]]
n=4
elim_mat=[]
not_matched = 0
status = 0
def createBaseMatrix(n):
    global board,queenPosition
    board=[]
    queenPosition=[]
    for i in range(0, int(n)):
        ln = []
        for j in range(0, int(n)):
            ln.append(0)
        board.append(ln)
        queenPosition.append([-1, -1])

# method have 3 parameters, no = queen number, r = row, c= column
def placeQueen(no,r,c):
    queenPosition[no] = (r,c)

# def addToEliminate(r,c):
#
#     for rw in elimination_mat:
#         if elimination_mat[rw][0] != r and elimination_mat[rw][1] != c:
#             elimination_mat.append(r.__str__ + c.__str__)

def checkRowColumnlogic(rw,cl,new_r,new_c,n):
    global not_matched
    if rw == new_r or cl == new_c:
        not_matched += 1
    elif rw == -1 or cl == -1:
        pass
    else:
        for num in range(0,new_r+1):
            if new_r == rw + num and new_c == cl + num:
                not_matched += 1
            elif new_r == rw + num and new_c == cl - num:
                not_matched += 1

        for num in range(new_r,n):
            if new_r == rw - num and new_c == cl - num:
                not_matched += 1
            elif new_r == rw - num and new_c == cl + num:
                not_matched += 1

def checkConditions(no,r,c,n):
    global not_matched
    not_matched = 0
    if no == 0:
        placeQueen(no,r,c)
        return 1
    else:
        for qn in queenPosition:
            checkRowColumnlogic(qn[0],qn[1],r,c,n)
            if not_matched !=0:
                break

        if not_matched == 0:
            placeQueen(no,r,c)
            return 1
        else:
            return 0

def checkCellElimination(rw,cl):
    for i in elim_mat:
        if i[0] == rw and i[1] ==cl:
            return True

    return False

def checkAllQueensFilled(queenPosition):
    for qn in queenPosition:
        if qn[0] == -1 or qn[1] == -1:
            return True

    return False

def printResult():
    for qn in queenPosition:
        board[qn[0]][qn[1]]=1


    for r in board:
        for c in r:
            print(c,end=" ")
        print()
    print(queenPosition)

if __name__ == '__main__':

    createBaseMatrix(n)
    while (checkAllQueensFilled(queenPosition)):
        createBaseMatrix(n)
        for q in range(0, n):
            for r in range(0, n):
                for c in range(0, n):
                    # if (r == 0 and c == 0) or (r == 0 and c == 1):
                    if checkCellElimination(r, c):
                        pass
                    else:
                        status = checkConditions(q, r, c, n)
                        if status == 1:
                            break
                if status == 1:
                    break

        if checkAllQueensFilled(queenPosition):
            elim_mat.append([queenPosition[0][0], queenPosition[0][1]])

    printResult()