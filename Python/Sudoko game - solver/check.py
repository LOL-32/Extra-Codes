##Import
from backendfunction import *


###Print Board
def print_sudoku(board):
    count_1 = 0
    for i, row in enumerate(board):
        print((" {}   {}   {} |"*2 + " {}   {}   {} ").format(*[x if x != 0 else "  " for x in row]))
        if i % 3 == 2:
            count_1 = count_1 + 1
            if(count_1 < 3):
              print("-----------+"*2 + "-----------")

###Rows
def check_rows(x):
    b=[]
    count = 0
    for k in x:
        count = count + 1
        ans = check_duplicates(k)
        if(ans == False):
            b.append(count-1)
    if(len(b) > 0):
        print("... Rows ",b , " failed.")
    else:
        print("... Rows OK")
        return True

###Columns
def check_column(x):
    a=[]
    b=[]
    count = 0
    #print(x)
    for i in range(0,9):
        for j in x:
            a.append(j[i])
    c = convert_list_2(a)
    for k in c:
        count = count + 1
        ans = check_duplicates(k)
        if(ans == False):
          #print(a)
          a.clear()
          b.append(count-1)
    if(len(b) > 0):
        print("... Columns ",b , " failed.")
    else:
        print("... Columns OK")
        return True
    
###subgrids
def check_subgrids(x):
    a= [x[0],x[1],x[2],x[9],x[10],x[11],x[18],x[19],x[20]]
    b= [x[3],x[4],x[5],x[12],x[13],x[14],x[21],x[22],x[23]]
    c= [x[6],x[7],x[8],x[15],x[16],x[17],x[24],x[25],x[26]]
    d= [x[27],x[28],x[29],x[36],x[37],x[38],x[45],x[46],x[47]]
    e= [x[30],x[31],x[32],x[39],x[40],x[41],x[48],x[49],x[50]]
    f= [x[33],x[34],x[35],x[42],x[43],x[44],x[51],x[52],x[53]]
    g= [x[54],x[55],x[56],x[63],x[64],x[65],x[72],x[73],x[74]]
    h= [x[57],x[58],x[59],x[66],x[67],x[68],x[75],x[76],x[77]]
    i= [x[60],x[61],x[62],x[69],x[70],x[71],x[78],x[79],x[80]]
    l=[a,b,c,d,e,f,g,h,i]
    check = []
    count = 0 
    for i in l:
        count = count + 1
        ans = check_duplicates(i)
        if(ans == False):
            check.append(count-1)
    if(len(check) > 0):
        print("... Subgrids ",check , " failed.")
    else:
        print("... Subgrids OK")
        return True
