def Sets(x,y,z):
    if (z == 1):
       g=set(x).union(y)
       print ("Your Answer is = " ,g)
    if (z == 2):
       g=set(x).intersection(y)
       print ("Your Answer is = " ,g)
    if (z == 3):
       g=set(x).difference(y)
       print ("Your Answer is = " ,g)
    if (z == 4):
       print("Enter U set elements = ")
       w=[int(y) for y in input().split()]
       g=set(x).difference(y)
       h=set(w).union(g)
       print ("The answer of L.H.S == ",h)
       p=set(w).union(x)
       y=set(w).union(y)
       z=set(p).difference(y)
       print ("The answer of R.H.S == ",z)
    
       
print("\n Menu \n")
print("To find Union(A U B):        Press 1 \nTo find Intersection(A ∩ B): press 2 \nTo find Difference(A - B):   press 3 \nTo find U(A - B)==(UA-UB):   press 4")
z=int(input("Enter your Choice = "))
print ("\nPlease put one space b/w elements")
print("\nEnter A set elements = ")          
x=[int(x) for x in input().split()]
print("Enter B set elements = ")
y=[int(y) for y in input().split()]
    
Sets(x,y,z)

    
