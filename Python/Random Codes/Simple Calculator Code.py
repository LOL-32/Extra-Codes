### A Basic Calculator Code ###
### Calculator include Function of Division,Multiplicaion,Addition,Subtratcion ###

### Code start!!!!!!!! ###

###Notation use to donate "Divide,Multiply,Addition & Subtraction" ###
d="Divide"
m="Multiply"
a="Addition"
s="Subtract"
n="Nothing"

### Use "p" for donating Divide,Multiply,Addition,Subtraction ###
Choice=Divide="d"
Choice=Multiply="m"
Choice=Addition="a"
Choice=Subtract="s"
choice=Nothing="n"

print ("For Divide   press d" )                      ##
print ("For Multiply press m" )                      ##
print ("For Addition press a" )                      ####  Use print command to give choice to user  
print ("For Subtract press S" )                      ####
print ("For Nothing  press n" )                      ##
print ("For Exit     press e" )                      ##
Choice= str (input("what you want to do??? "))
 

if Choice=="d":
       e= int (input("Enter a number e: "))          ##
       f= int (input("Enter a number f: "))          ##
       def Divide(e , f):                            ####  Division 
              return e / f                           ####
       x=Divide (e, f)                               ##
       print ("Division of given number is= " , x)   ##


     
if Choice=="m":
       g= int (input("Enter a number g: "))          ##	   
       h= int (input("Enter a number h: "))          ##
       def Multiply(g , h):	                     ####  Multiplicaion
              return g * h                           ####
       y=Multiply (g , h)                            ##
       print ("Multiply of given number is= " , y)   ## 


if Choice=="a":
       a= int (input("Enter a number a: "))          ## 
       b= int (input("Enter a number b: "))          ####  Sum
       V= sum( [a , b] )                             ####
       print ("Addition of given number is= " , V)   ##
 
if Choice=="s":
       c= int (input("Enter a number c: "))          ##
       d= int (input("Enter a number d: "))          #### Subtract 
       w== sum( [a , -b] )                           ####
       print ("Subtration of given number is= " , w) ##

if Choice=="n":                                      ##   Nothing
       print ("Ok! Have a good time")                ##

if choice=="e":                                      ##   Exit
       exit()                                        ##


###  Code End!  ###




