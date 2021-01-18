##Variables 
sudoku_list = []
column_list    = []

#####Backend Functions

#Conversion Functions 
def convert_list_1(x):
    a=x[0:9]
    b=x[9:18]
    c=x[18:27]
    d=x[27:36]
    e=x[36:45]
    f=x[45:54]
    g=x[54:63]
    h=x[63:72]
    i=x[72:81]
    sudoku_list.append(a)
    sudoku_list.append(b)
    sudoku_list.append(c)
    sudoku_list.append(d)
    sudoku_list.append(e)
    sudoku_list.append(f)
    sudoku_list.append(g)
    sudoku_list.append(h)
    sudoku_list.append(i)


def convert_list_2(x):
    a=x[0:9]
    b=x[9:18]
    c=x[18:27]
    d=x[27:36]
    e=x[36:45]
    f=x[45:54]
    g=x[54:63]
    h=x[63:72]
    i=x[72:81]
    column_list.append(a)
    column_list.append(b)
    column_list.append(c)
    column_list.append(d)
    column_list.append(e)
    column_list.append(f)
    column_list.append(g)
    column_list.append(h)
    column_list.append(i)
    return column_list



#Check Duplicates
def check_duplicates(x):
    a=[]
    for i in x:
        if(i != 0):
         a.append(x.count(i))
    for j in a:
        if(j > 1):
            return False
    return True

        
