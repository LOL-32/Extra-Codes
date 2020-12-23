
def display_matrix(x,l):
    
    a=0
    for i in range(0,len(l)):
     print(" ",l[i],end="|")
     a=a+1
     if(a== (x)):
        print(end="\n")
        a=0
        
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

def addition(w,x,y,z,a,b):
    if(w ==y and x ==z):
       c=[]
       print("Matrix 1")
       display_matrix(x,a)
            
       print("Matrix 2")
       display_matrix(z,b)

       d=conv1(a,x)
       e=conv1(b,z)

       print(d)
       print(e)

       for i in range(0,w):
          for k in range(0,z):
              l=d[i][k] + e[i][k]
              c.append(l)
       print("Answer is : ")
       display_matrix(z,c)
    else:
    	print("Matrix cannot be added")

def subtraction(w,x,y,z,a,b):
    if(w ==y and x ==z):
        c=[]
        print("Matrix 1")
        display_matrix(x,a)
            
        print("Matrix 2")
        display_matrix(z,b)
        d=conv1(a,x)
        e=conv1(b,z)

        print(d)
        print(e)

        for i in range(0,w):
          for k in range(0,z):
              l=d[i][k] - e[i][k]
              c.append(l)
        
              

        
        print("Answer is : ")
        display_matrix(z,c)
        return
    else:
    	print("Matrix cannot be subtarcted")



###Test Case
#addition(2,2,2,2,[1,2,3,4],[5,6,7,8])
#addition(3,2,3,2,[1,2,3,4,5,9],[5,6,7,8,9,10,11,12])
#addition(3,2,3,2,[1,2,3,4,5,6],[7,8,9,10,11,12])
#addition(3,3,3,3,[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,15,17,18])
#addition(2,3,2,3,[1,2,3,4,5,9],[5,6,7,8,9,10,11,12])


#subtraction(2,2,2,2,[1,2,3,4],[5,6,7,8])
#subtraction(3,2,3,2,[1,2,3,4,5,9],[5,6,7,8,9,10,11,12])
#subtraction(3,2,3,2,[1,2,3,4,5,6],[7,8,9,10,11,12])
#subtraction(3,3,3,3,[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,15,17,18])
#subtraction(2,3,2,3,[1,2,3,4,5,9],[5,6,7,8,9,10,11,12])

