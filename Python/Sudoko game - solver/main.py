##Import 
import csv
from backendfunction import *
from check import *



###Main Code   
def read_data_from_csv(filename):
    l=[]
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            a=(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]}')
            for i in a:
                if(i != ' '):
                   l.append(int(i))
    return l
               

if __name__ == '__main__':
    file_name = str(input("Enter file name : "))
    x=(read_data_from_csv( file_name))
    convert_list_1(x)
    print_sudoku(sudoku_list)
    print("\nChecking puzzle .....")
    check_1 = check_rows(sudoku_list)
    check_2 = check_column(sudoku_list)
    check_3 = check_subgrids(x)
    if(check_1 == True and check_2 == True and check_3 == True):
        print("Partial Puzzle solution is correct!")
    else:
        print("Complete Puzzle solution is NOT correct.")














