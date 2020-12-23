
def factors(x):
  l=[]
  for i in range(2,x+1):
        if (x % i) == 0:
           z=i
           if (z == x):
               continue
           else:
             l.append(i)
             
  print ('Factors are = ' , l)

y=int(input("Enter a Number = "))            
factors(y)
