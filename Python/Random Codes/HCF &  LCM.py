def HCFandLCm(x,y,z):
    if (z == 1):
     l=[]
     m=[]
     for i in range(1,x):
      if(x % i == 0):
          z=l.append(i)
    
     for i in range(1,y):
        if(y % i == 0):
          z=m.append(i)


     j=list(set(l).intersection(m))
     print  (max(j))

    if (z == 2):
      l=[]
      m=[]
      for i in range(1,x):
        if(x % i == 0):
          z=l.append(i)
    
      for i in range(1,y):
        if(y % i == 0):
          z=m.append(i)

      j=list(set(l).intersection(m))
      print  ((j))



HCFandLCm(18,24,2)
