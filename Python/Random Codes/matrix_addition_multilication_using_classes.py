class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix

    def __mul__(self,other):
        temp_1= []
        for i in self.matrix:
            temp_1.append(len(i))
        column_of_a_matrix = (list(set(temp_1))[0])
        row_of_b_matrix    =(len(other.matrix))

        if(column_of_a_matrix == row_of_b_matrix ):
            result=[]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    b = 0
                    for k in range(len(other.matrix)):
                       b += self.matrix[i][k] * other.matrix[k][j]
                    result.append(b)
            return Matrix(result)
        else:
            print("ValueError : inner dimension should be the same size")

    def __add__(self,other):
        temp_1= []
        temp_2= []
        for i in self.matrix:
            temp_1.append(len(i))
        column_of_a_matrix = (list(set(temp_1))[0])

        for i in other.matrix:
            temp_2.append(len(i))
        column_of_b_matrix = (list(set(temp_2))[0])

        row_of_a_matrix =(len(self.matrix))
        row_of_b_matrix =(len(other.matrix))
        
        if(row_of_a_matrix == row_of_b_matrix  and column_of_a_matrix == column_of_b_matrix ):
            result=[]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    b = self.matrix[i][j] + other.matrix[i][j]
                    result.append(b)
            return Matrix(result)
        else:
            print("ValueError : dimension should be the same size")

    def __str__(self):
         return str(self.matrix)
    
    def shape(self):
        p = list(self.matrix)
        t = ()
        count = 0
        if any(isinstance(x, list) for x in p):
            t = t +tuple(str(len(p)))
            for i in self.matrix:
                for j in i:
                    count = count + 1
            return t

        else:
            t = t + tuple('1')
            for i in self.matrix:
                count = count + 1

            t = t + tuple(str(count))
            return t


    

    

if __name__ == "__main__":
    # Uncomment the following sections as you
    # fill in the Matrix class
    # # set up the matrices

    
    A = Matrix([[1,2,3],[4,5,6]])

    B = Matrix([[1,2],[3,4],[5,6]])
    C = Matrix([[1,2,3],[4,5,6]])

    # # do the computation
    
    D = A*B
    E = A+C

    F= Matrix([[1,2,3],[4,5,6]])

    # # print the attibutes
    print("D.shape = " ,D.shape())
    
    # # print the results
    print("A*B =")
    print("%s" % D)
    print("A+C =")
    print("%s" % E)

    
        
