### A Basic Calculator Code ###
### Calculator include Function of Division,Multiplicaion,Addition,Subtratcion ###
### Code start!!!!!!!! ###
###Notation use to donate "Divide,Multiply,Addition & Subtraction" ###
d="Divide"
m="Multiply"
a="Addition"
s="Subtract"
n="Nothing"
sin="SIN"
cos="COS"
tan="TAN"
### Use "p" for donating Divide,Multiply,Addition,Subtraction ###
Choice=Divide="d"
Choice=Multiply="m"
Choice=Addition="a"
Choice=Subtract="s"
Choice=Nothing="n"
Choice=SIN="sin" or "SIN"
Choice=COS="cos" or "COS"
Choice=TAN="tan" or "TAN"
###START###
print ("For Divide   press d" )                      
print ("For Multiply press m" )                     
print ("For Addition press a" )                       
print ("For Subtract press S" )
print ("For SIN  press Sin" )
print ("For COS  press cos" )
print ("For TAN  press tan" )
print ("For Nothing  press n" )                      
print ("For Exit     press e" )                      

Choice= str (input("what you want to do??? "))

if Choice=="d":
       e= int (input("Enter a number e: "))         
       f= int (input("Enter a number f: "))         
       def Divide(e , f):                          
              return e / f                           
       x=Divide (e, f)                              
       print ("The answer is = "  , x)   

if Choice=="m":
       g= int (input("Enter a number g: "))          
       h= int (input("Enter a number h: "))         
       def Multiply(g , h):	                     
              return g * h                           
       y=Multiply (g , h)                            
       print ("The answer is = "  , y)  

if Choice=="a":
       a= int (input("Enter a number a: "))          
       b= int (input("Enter a number b: "))          
       z= sum( [a , b] )                             
       print ("The answer is = "  , V)   
 
if Choice=="s":
       c= int (input("Enter a number c: "))          
       d= int (input("Enter a number d: "))           
       w== sum( [a , -b] )                          
       print ("The answer is = "  , w)

if Choice=="sin":
       import math
       i= int (input("Enter a number e: "))
       y=math.sin(i)
       print ("The answer is = " , y)

if Choice=="cos":
       import math
       i= int (input("Enter a number e: "))
       y=math.cos(i)
       print ("The answer is = " , y)

if Choice == "tan":
       import math
       x=int(input("Enter a number = "))
       if (x == 90):
            print ("Undefined ")
       else:
             y=math.tan(x)
             print ("The answer is = "  ,y)
       
if Choice=="n":                                      
       print ("Ok! Have a good time")                

if Choice=="e":                                      
       exit()                                       







