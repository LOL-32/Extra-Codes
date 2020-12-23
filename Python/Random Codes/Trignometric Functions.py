print("##Important Notes##")
print("Please Enter VALUE in RADIANS")
print(" For calculation of SIN enter sin \n For calculation of COS enter cos \n For calculation of TAN enter tan")
      


def trignometricfunction(trig):
    sin = 'sin'
    cos = 'cos'
    tan = 'tan'
    import math
    trig=str(input("Enter want you want o calculate = "))
    if (trig == 'sin'):
         x=int(input("Enter a number = "))
         y=math.sin(x)
         print ("The answer is = " ,y)
         print (" :) ")

    if (trig == 'cos'):
         x=int(input("Enter a number = "))
         y=math.cos(x)
         print ("The answer is = " ,y)
         print (" :) ")
    if (trig == 'tan'):
        x=int(input("Enter a number = "))
        if (x == 90):
            print ("Undefined ")
            print (" :( ")
        else:
             y=math.tan(x)
             print ("The answer is = " ,y)
             print (" :) ")
    


trignometricfunction(1)
