import random
mainboard = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]

row1 = mainboard[0]
row2 = mainboard[1]
row3 = mainboard[2]
row4 = mainboard[3]
row5 = mainboard[4]
row6 = mainboard[5]
row7 = mainboard[6]
row8 = mainboard[7]
row9 = mainboard[8]

def Square1():
    while True:
        sq1 = [mainboard[0][0],mainboard[0][1],mainboard[0][2],mainboard[1][0],mainboard[1][1],mainboard[1][2],mainboard[2][0],mainboard[2][1],mainboard[2][2]]
        count = 0
        row_move = random.randrange(0,3)
        column_move = random.randrange(0,3)
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq1)
        for item in sq1:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break    

def Square2():
    while True:
        sq2 = [mainboard[0][3],mainboard[0][4],mainboard[0][5],mainboard[1][3],mainboard[1][4],mainboard[1][5],mainboard[2][3],mainboard[2][4],mainboard[2][5]]
        count = 0
        row_move = random.randrange(0,3)
        column_move = random.randrange(0,3)
        column_move = column_move+3
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq2)
        for item in sq2:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break
        
def Square3():
    while True:
        sq3 = [mainboard[0][6],mainboard[0][7],mainboard[0][8],mainboard[1][6],mainboard[1][7],mainboard[1][8],mainboard[2][6],mainboard[2][7],mainboard[2][8]]
        count = 0
        row_move = random.randrange(0,3)
        column_move = random.randrange(0,3)
        column_move = column_move + 6
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq3)
        for item in sq3:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break

def Square4():
    while True:
        sq4 = [mainboard[3][0],mainboard[3][1],mainboard[3][2],mainboard[4][0],mainboard[4][1],mainboard[4][2],mainboard[5][0],mainboard[5][1],mainboard[5][2]]
        count = 0
        row_move = random.randrange(0,3)
        row_move = row_move+3
        column_move = random.randrange(0,3)
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq4)
        for item in sq4:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break

def Square5():
    while True:
        sq5 = [mainboard[3][3],mainboard[3][4],mainboard[3][5],mainboard[4][3],mainboard[4][4],mainboard[4][5],mainboard[5][3],mainboard[5][4],mainboard[5][5]]
        count = 0
        row_move = random.randrange(0,3)
        row_move = row_move+3
        column_move = random.randrange(0,3)
        column_move = column_move+3
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq5)
        for item in sq5:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break

def Square6():
    while True:
        sq6 = [mainboard[3][6],mainboard[3][7],mainboard[3][8],mainboard[4][6],mainboard[4][7],mainboard[4][8],mainboard[5][6],mainboard[5][7],mainboard[5][8]]
        count = 0
        row_move = random.randrange(0,3)
        row_move = row_move + 3
        column_move = random.randrange(0,3)
        column_move = column_move +6
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq6)
        for item in sq6:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break 

def Square7():
    while True:
        sq7 = [mainboard[6][0],mainboard[6][1],mainboard[3][2],mainboard[7][0],mainboard[7][1],mainboard[7][2],mainboard[8][0],mainboard[8][1],mainboard[8][2]]
        count = 0
        row_move = random.randrange(0,3)
        row_move = row_move + 6
        column_move = random.randrange(0,3)
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq7)
        for item in sq7:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break 

def Square8():
    while True:
        sq8 = [mainboard[6][3],mainboard[6][4],mainboard[3][5],mainboard[7][3],mainboard[7][4],mainboard[7][5],mainboard[8][3],mainboard[8][4],mainboard[8][5]]
        count = 0
        row_move = random.randrange(0,3)
        row_move = row_move + 6
        column_move = random.randrange(0,3)
        column_move = column_move +3
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq8)
        for item in sq8:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break 

def Square9():
    while True:
        sq9 = [mainboard[6][6],mainboard[6][7],mainboard[3][8],mainboard[7][6],mainboard[7][7],mainboard[7][8],mainboard[8][6],mainboard[8][7],mainboard[8][8]]
        count = 0
        row_move = random.randrange(0,3)
        row_move = row_move + 6
        column_move = random.randrange(0,3)
        column_move = column_move +6
        number = random.randrange(1,10)
        A = check_row_column(number,row_move,column_move)
        B = square_check(number,sq9)
        for item in sq9:
            if item != 0:
                count = count + 1
        C = count < 3
        D = mainboard[row_move][column_move] == 0
        print(D)
        print(row_move,column_move,number)
        if A and B and C and D:
            mainboard[row_move][column_move] = number
            for item in mainboard:
                print(item)
        if count>=3:
            break 

def check_row_column(number,row_move,column_move):
    row_check = True
    column_check = True
    column = [
    [mainboard[0][0],mainboard[1][0],mainboard[2][0],mainboard[3][0],mainboard[4][0],mainboard[5][0],mainboard[6][0],mainboard[7][0],mainboard[8][0]],
    [mainboard[0][1],mainboard[1][1],mainboard[2][1],mainboard[3][1],mainboard[4][1],mainboard[5][1],mainboard[6][1],mainboard[7][1],mainboard[8][1]],
    [mainboard[0][2],mainboard[1][2],mainboard[2][2],mainboard[3][2],mainboard[4][2],mainboard[5][2],mainboard[6][2],mainboard[7][2],mainboard[8][2]],
    [mainboard[0][3],mainboard[1][3],mainboard[2][3],mainboard[3][3],mainboard[4][3],mainboard[5][3],mainboard[6][3],mainboard[7][3],mainboard[8][3]],
    [mainboard[0][4],mainboard[1][4],mainboard[2][4],mainboard[3][4],mainboard[4][4],mainboard[5][4],mainboard[6][4],mainboard[7][4],mainboard[8][4]],
    [mainboard[0][5],mainboard[1][5],mainboard[2][5],mainboard[3][5],mainboard[4][5],mainboard[5][5],mainboard[6][5],mainboard[7][5],mainboard[8][5]],
    [mainboard[0][6],mainboard[1][6],mainboard[2][6],mainboard[3][6],mainboard[4][6],mainboard[5][6],mainboard[6][6],mainboard[7][6],mainboard[8][6]],
    [mainboard[0][7],mainboard[1][7],mainboard[2][7],mainboard[3][7],mainboard[4][7],mainboard[5][7],mainboard[6][7],mainboard[7][7],mainboard[8][7]],
    [mainboard[0][8],mainboard[1][8],mainboard[2][8],mainboard[3][8],mainboard[4][8],mainboard[5][8],mainboard[6][8],mainboard[7][8],mainboard[8][8]],
    ]
    if number in mainboard[row_move]:
        row_check = False
    if number in column[column_move]:
        column_check = False
    if row_check and column_check :
        return True
    else:
        return False
def square_check(number,sq):
    square_check = True
    if number in sq:
        square_check = False
    return square_check

Square1()
Square2()
Square3()
Square4()
Square5()
Square6()
Square7()
Square8()
Square9()

#for item in range(9):
    #for i in range(9):
     #   if mainboard[item][i] == 0:
      #      pass
       # else:
        #    mainboard[item][i] = str(mainboard[item][i])
for item in mainboard:
    print(item,end=",")
    print()