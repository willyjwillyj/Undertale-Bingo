import random, json, os, sys, math
dir = os.path.dirname(sys.executable)
goalsdir = os.path.join(dir, "goals.txt")
print(goalsdir)
filename_error = False
try:
    f = open(goalsdir, "r")
    goalsunsorted = f.readlines()
    f.close()
except:
    filename_error = True
running = True

def setup():
    global empty, difmap, goals, board, cats
    empty = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    difmap = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    goals = []
    board = []
    cats = [[],[],[]]

def sortgoals():
    global cats
    cats = [[],[],[]]
    for i in goalsunsorted:
        try:
            dif = int(i[0])
            try:
                cats[dif-1].append(i[2:])
            except IndexError:
                print(f"Unsuported difficulty: {dif} on item {i[2:]}")
        except ValueError:
            print(f"Uncategorized goal \"{i}\"")

def setthrees():
    global difmap, empty
    available = [
    [0, 1, 2, 3, 4 ],
    [5, 6, 7, 8, 9 ],
    [10,11,12,13,14],
    [15,16,17,18,19],
    [20,21,22,23,24]
    ]
    #pick positive diagonal position
    pos = random.randint(0,4)
    empty.remove(5*pos + pos)
    difmap[pos][pos] = 3
    if pos == 2:
        #center cell chosen
        flip = random.randint(0,1)
        if flip == 0:
            difmap[0][1] = 3
            difmap[1][4] = 3
            difmap[3][0] = 3
            difmap[4][3] = 3
            empty.remove(1)
            empty.remove(9)
            empty.remove(15)
            empty.remove(23)
        else:
            difmap[0][3] = 3
            difmap[1][0] = 3
            difmap[3][4] = 3
            difmap[4][1] = 3
            empty.remove(3)
            empty.remove(5)
            empty.remove(19)
            empty.remove(21)
    else:
        #remove cells in row/col/dia from posible locations
        row = pos
        col = pos
        for i in range(0,5):
            if i == row:
                available[i] = []
            else:
                try:
                    available[i].remove(5*i + col)
                except ValueError:
                    pass
                try:
                    available[i].remove(5*i + i)
                except ValueError:
                    pass
        #select position on nevative diagonal
        flip = random.randint(0,1)
        if flip == 0:
            #higher cell chosen
            if pos == 0 or pos == 4:
                #positive diagonal 3 is in corner
                row = 1
                col = 3
            else:
                #positive diagonal 3 is in wing
                row = 0
                col = 4
        else:
            #lower cell chosen
            if pos == 0 or pos == 4:
                #positive diagonal 3 is in corner
                row = 3
                col = 1
            else:
                #positive diagonal 3 is in wing
                row = 4
                col = 0
        #remove cells in row/col/dia from posible locations
        empty.remove(5*row + col)
        difmap[row][col] = 3
        for i in range(0,5):
            if i == row:
                available[i] = []
            else:
                try:
                    available[i].remove(5*i + col)
                except ValueError:
                    pass
                try:
                    available[i].remove(5*i + 4 - i)
                except ValueError:
                    pass
        #chose one of the two remaining boards
        flip = random.randint(0,1)
        #find first row with no 3
        i = 0
        while True:
            if len(available[i]) == 2:
                break
            else:
                i += 1
        row = i
        col = available[i][flip] % 5
        difmap[row][col] = 3
        #remove cells in row/col from available list
        empty.remove(5*row + col)
        for i in range(0,5):
            if i == row:
                available[i] = []
            else:
                try:
                    available[i].remove(5*i + col)
                except ValueError:
                    pass
        #set remaining board
        for j in range(0,2):
            #find row with only one available cell
            i = 0
            while True:
                if len(available[i]) == 1:
                    break
                else:
                    i += 1
            row = i
            col = available[i][0] % 5
            difmap[row][col] = 3
            #remove cells in row/col from available list
            empty.remove(5*row + col)
            for i in range(0,5):
                if i == row:
                    available[i] = []
                else:
                    try:
                        available[i].remove(5*i + col)
                    except ValueError:
                        pass

def setones():
    global difmap, empty
    available = [
    [0, 1, 2, 3, 4 ],
    [5, 6, 7, 8, 9 ],
    [10,11,12,13,14],
    [15,16,17,18,19],
    [20,21,22,23,24]
    ]
    dia = []
    #remove cells containing 3s from available cells
    for i in range(0,5):
        for j in range(0,5):
            if 5*i + j not in empty:
                available[i].remove(available[i][j])
    #find posible locations on positive diagonal
    for i in range(0,5):
        if (5*i + i) in available[i]:
            dia.append(5*i + i)
    #chose location on posiive diagonal
    roll = random.randint(0,3)
    loc = dia[roll]
    row = math.floor(loc/5)
    col = loc % 5
    empty.remove(loc)
    difmap[row][col] = 1
    if row == 2:
        #center cell chosen
        r = False
        l = False
        #check if right permutation is available
        if 3 in empty and 5 in empty and 19 in empty and 21 in empty:
            r = True
        #check if left permutation is available
        if 1 in empty and 14 in empty and 15 in empty and 23 in empty:
            l = True
        if r == True and l == True:
            #both available
            flip = random.randint(0,1)
            if flip == 0:
                r == False
        if r == False:
            #l chosen
            difmap[0][1] = 1
            difmap[1][4] = 1
            difmap[3][0] = 1
            difmap[4][3] = 1
            empty.remove(1)
            empty.remove(9)
            empty.remove(15)
            empty.remove(23)
        else:
            difmap[0][3] = 1
            difmap[1][0] = 1
            difmap[3][4] = 1
            difmap[4][1] = 1
            empty.remove(3)
            empty.remove(5)
            empty.remove(19)
            empty.remove(21)
    else:
        #remove cells in row/col/dia from available list
        dia = []
        #remove cases where no board is posible
        if difmap[2][2] == 3:
            if difmap[0][1] == 3:
                if difmap [0][0] == 1:
                    available[3].remove(16)
                elif difmap[4][4] == 1:
                    available[1].remove(8)
                elif difmap[1][1] == 1:
                    available[0].remove(4)
                elif difmap[3][3] == 1:
                    available[4].remove(20)
            else:
                if difmap [0][0] == 1:
                    available[1].remove(8)
                elif difmap[4][4] == 1:
                    available[3].remove(16)
                elif difmap[1][1] == 1:
                    available[4].remove(20)
                elif difmap[3][3] == 1:
                    available[0].remove(4)
        for i in range(0,5):
            if i == row:
                available[i] = []
            else:
                try:
                    available[i].remove(5*i + col)
                except ValueError:
                    pass
                try:
                    available[i].remove(5*i + i)
                except ValueError:
                    pass
            #get available positions for negative diagonal
            if 5*i + 4 - i in available[i]:
                dia.append(5*i + 4 - i)
        #chose location on negative diagonal
        roll = random.randint(0,len(dia)-1)
        loc = dia[roll]
        row = math.floor(loc/5)
        col = loc % 5
        difmap[row][col] = 1
        #remove cells in row/col/dia from available list
        empty.remove(loc)
        for i in range(0,5):
            if i == row:
                available[i] = []
            else:
                try:
                    available[i].remove(5*i + col)
                except ValueError:
                    pass
                try:
                    available[i].remove(5*i + 4 - i)
                except ValueError:
                    pass
        #set remaining options
        for x in range(0,3):
            #find row with fewest options
            min = 5
            minrow = 0
            for i in range(0,5):
                if min > len(available[i]) > 0:
                    min = len(available[i])
                    minrow = i
            roll = random.randint(0,len(available[minrow]) - 1)
            loc = available[minrow][roll]
            row = math.floor(loc/5)
            col = loc % 5
            difmap[row][col] = 1
            #remove cells in row/col from available list
            empty.remove(loc)
            for i in range(0,5):
                if i == row:
                    available[i] = []
                else:
                    try:
                        available[i].remove(5*i + col)
                    except ValueError:
                        pass

def filltwos():
    global difmap
    for i in range(0,5):
        for j in range(0,5):
            if difmap[i][j] == 0:
                difmap[i][j] = 2

def gridgen():
    global goals, board, cats
    for i in range(0,5):
        for j in range(0,5):
            dif = difmap[i][j] - 1
            n = len(cats[dif]) - 1
            randgoal = cats[dif][random.randint(0,n)]
            print(n)
            goals.append(randgoal)
            cats[dif].remove(randgoal)
    for i in range(0,25):
        board.append({'name': goals[i]})
    print("\n\n")
    return(json.dumps(board))

while False:
    reading = True
    while reading:
        gen = input("Generate grid? Y/N\n")
        if(gen == "y" or gen == "Y"):
            reading = False
        elif(gen == "n" or gen == "N"):
            running = False
            reading = False
        else:
            print("Invalid response\n")
    if(not running):
        break
    setup()
    sortgoals()
    setthrees()
    setones()
    filltwos()
    gridgen()
    print("\n\n")

def genProcess():
    setup()
    sortgoals()
    setthrees()
    setones()
    filltwos()
    return gridgen()