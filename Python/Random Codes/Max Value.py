w=int (input("Enter a value w = "))
x=int (input("Enter a value x = "))
y=int (input("Enter a value y = "))
z=int (input("Enter a value z = "))

def max1(w , x , y , z):
     def max2(m , n):
         if m > n:
             return m
         else:
             return n
     a=max2(w , x)
     b=max2(y , z)
     c=max2(a , b)
     f=print ("Maximum value is = " , c)
     return f
(max1(w , x ,y , z))
