a=int (input("Enter a number A= "))
b=int (input("Enter a number B= "))
c=int (input("Enter a number C= "))

from math import sqrt

x = (b^2 - 4 * a * c)

print (x)
if x > 0:
   from math import sqrt
   print(-b + sqrt(b^2 - 4 *a *c))  / 2 *a 
   print(-b - sqrt(b^2 - 4 *a *c))  / 2 *a 

if x == 0:
   from math import sqrt
   print (-b + sqrt(b^2 - 4 *a *c))  / 2 *a
   print (-b - sqrt(b^2 - 4 *a *c))  / 2 *a
if x < 0:
   print ("Roots Are complex")


