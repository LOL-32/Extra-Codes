def prime(x):
 if x > 1:
  for i in range(2,x):
    if (x % i) == 0:
      return 
  else:
      return (x)




def factors(x):
  l=[]
  for i in range(2,x+1):
        if (x % i) == 0:
            z=(prime(i))
            if z == None:
                continue
            else:
               l.append(z)
  print ("Prime Factors of Number are =",l)
            
    
        
f=int(input("Enter a number = "))
factors(f)
