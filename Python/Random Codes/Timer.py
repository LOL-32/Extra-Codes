import time
import os
import sys



def timer():
    os.system('cls')
    n=59
    
    while(n >= 0):
     time.sleep(1)
     os.system('cls')
     print(" wait ",n," Second ")
     n=n-1

timer()
os.system("pause")
