###Side Function
def  conv1(a,w):
        temp=[]
        count=0
        t=[]
        for i in a:
           count = count +1
           t.append(i)
           if(count == (w)):
               temp.append(list(t))
               t.clear()
               count=0
        return temp

def  conv2(a,w):
        temp=[]
        count=0
        t=[]
        for i in a:
           count = count +1
           t.append(i)
           if(count == (w)):
               temp.append(list(t))
               t.clear()
               count=0
        return transpose(temp,w)
        
                

###Display Function 
def display_matrix(x,l):
    
    a=0
    for i in range(0,len(l)):
     print(" ",l[i],end="|")
     a=a+1
     if(a== (x)):
        print(end="\n")
        a=0
###Transpose
def  transpose(l,w):
     t=[]
     temp=[]
     for i in range(0,w,1):
      for j in l:
        t.append(j[i])
      temp.append(list(t))
      del t[:]
     return temp

       
def multiply_matrix(w,x,y,z,a,b):
    if(x==y):
        c=[]
        temp=[]
        print("Matrix 1")
        display_matrix(x,a)
        print("Matrix 2")
        display_matrix(z,b)
        
        d=conv1(a,x)
        e=conv2(b,z)

        len_a=len(d)
        
        for i in range(0,w):
         for j in range(0,z):
            for k in range(0,y):
              l=d[i][k]*e[j][k]
              temp.append(l)
            sum_variables =sum(temp)
            c.append(sum_variables)
            del temp[:]

        print("")
        print("")
        print("Answer is : ")
        display_matrix(z,c)
        
    else:
        print("Matrix cannot be Multiply")
           



####TEST CASE 
#multiply_matrix(2,2,2,2,[1,2,3,4],[1,2,3,4])
#multiply_matrix(1,3,3,2,[1,2,3],[1,2,3,4,5,6])
#multiply_matrix(2,2,2,2,[1,2,3,4],[1,2,3,4])


    
    
    
