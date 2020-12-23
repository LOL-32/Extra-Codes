print("##Important Numbers##")
print("Plz enter one number addition in range \n like i need table of 2 until 10 i will enter 11")

def table(x,y):
    for i in range(1 ,y):
        print(x, "x" , i , "=" , x*i)



a=int(input("Enter a number for table = "))
b=int(input("Enter a range of table = "))
table(a,b)
