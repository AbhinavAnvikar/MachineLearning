from array import *

"""
Algorithm -
 Regression model. Place queens sequentially and verify.

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# Created queenPosition with 4
queenPosition = [(-1,-1),(-1,-1),(-1,-1),(-1,-1)]
"""
board=[]
queenPosition=[]
n=4
def createBaseMatrix(n):
    for i in range(0, int(n)):
        ln = []
        for j in range(0, int(n)):
            ln.append(0)
        board.append(ln)
        queenPosition.append([-1, -1])

elim_mat=[]

not_matched = 0
status = 0
# method have 3 parameters, no = queen number, r = row, c= column
def placeQueen(no,r,c):
    queenPosition[no] = (r,c)

# def addToEliminate(r,c):
#
#     for rw in elimination_mat:
#         if elimination_mat[rw][0] != r and elimination_mat[rw][1] != c:
#             elimination_mat.append(r.__str__ + c.__str__)

def checkRowColumnlogic(rw,cl,new_r,new_c):
    global not_matched
    if rw == new_r or cl == new_c:
        not_matched += 1
    elif rw == -1 or cl == -1:
        pass
    else:
        for n in range(0,new_r+1):
            if new_r == rw + n and new_c == cl + n:
                not_matched += 1
            elif new_r == rw + n and new_c == cl - n:
                not_matched += 1

        for n in range(new_r,4):
            if new_r == rw - n and new_c == cl - n:
                not_matched += 1
            elif new_r == rw - n and new_c == cl + n:
                not_matched += 1

def checkConditions(no,r,c):
    global not_matched
    not_matched = 0
    if no == 0:
        placeQueen(no,r,c)
        return 1
    else:
        for qn in queenPosition:
            checkRowColumnlogic(qn[0],qn[1],r,c)
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


# checkConditions(0,0,1)
# not_matched ==0
# checkConditions(1,1,3)
# not_matched ==0
# checkConditions(2,2,0)
# not_matched ==0
# checkConditions(3,3,2)
# not_matched ==0


createBaseMatrix(n)
while(checkAllQueensFilled(queenPosition)):
    queenPosition = [(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
    for q in range(0, 4):
        for r in range(0,4):
            for c in range(0,4):
                #if (r == 0 and c == 0) or (r == 0 and c == 1):
                if checkCellElimination(r,c):
                    pass
                else:
                    status = checkConditions(q,r,c)
                    if status == 1:
                        break
            if status == 1:
                break

    if checkAllQueensFilled(queenPosition):
        elim_mat.append([queenPosition[0][0],queenPosition[0][1]])


for qn in queenPosition:
    board[qn[0]][qn[1]]=1


for r in board:
    for c in r:
        print(c,end=" ")
    print()
print(queenPosition)