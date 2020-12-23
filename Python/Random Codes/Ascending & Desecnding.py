def fun(x):
   if(x == 'A'):
       l=[]
       r=int(input("Total number of numbers = "))
       for i in range(1,r):
           y=int(input("Enter number = "))
           l.append(y)
   print(sorted(l))
   if(x == 'D'):
       l=[]
       r=int(input("Total number of numbers = "))
       for i in range(1,r):
           y=int(input("Enter number = "))
           l.append(y)
   print(sorted(l ,reverse=False))
fun('D')
