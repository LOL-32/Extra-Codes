def sets(x,y):
     if (y == 0):
         print ("Null Set")
         print ("[0]")

     if (y == 1):
         l=[]
         print ("whole Number Set")
         for i in range(0,x+1):
             l.append(i)
         print(l)

     if (y == 2):
         l=[]
         print ("Integers Set")
         for i in range(x,0,-1):
            g=(-i)
            l.append(g)
         for i in range(0,x+1):
            l.append(i)
         print (l)
     if (y == 3):
         l=[]
         print ("Odd Number Set")
         for i in range(1,x,2):
             l.append(i)
         if (x % 2 != 0):
             l.append(x)
         print (l)
     if (y == 4):
         l=[]
         print ("Even Number Set")
         for i in range(0,x,2):
             l.append(i)
         if (x % 2 == 0):
             l.append(x)
         print (l)


print ("Choice")
print ("\n Press 0 for Null Set \n Press 1 for Whole Number Set \n Press 2 for Integers Set \n Press 3 for Odd Number Set \n Press 4 for Even Number Set")
x=int(input("\nEnter the Range of set = "))
y=int(input("\nEnter your Choice = "))


sets(x,y)
         
