import numpy as np



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
        
def det_2x2_matrix(a):
     value = ((a[0] * a[3]) - (a[1] * a[2]))
     return value

     
    

def det(w,x,a):
    display_matrix(x,a)

    if(w==x and w==2 ):
        c=[]
        display_matrix(x,a)
        print("\nDeterminent is : ",det_2x2_matrix(a))

    elif(w == x and w > 2):
        d= conv1(a,w)
        print (np.linalg.det(d))
        
       
#best way use numpy for det of nxn matrix

#Test Case
#det(3,3,[1,2,3,4,5,6,7,8,9])
