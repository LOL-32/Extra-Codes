def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def encryption(x,y):
    string_r      = reverse(x)
    encrypted_txt = ""
    for i in string_r:
        encrypted_txt += chr(ord(i)+int(y))
    return encrypted_txt

def decryption(x,y):
    string_r      = reverse(x)
    decrypted_txt = ""
    for i in string_r:
        decrypted_txt += chr(ord(i)-int(y))
    return decrypted_txt
    


def check_input(x,y):
    for i in x:
        if(ord(i) >= 97 and ord(i) <= 122):
            continue
        else:
            return False
    return True
    
    

x=str(input("Enter phrase to Encrypt (lowercase, no spaces): "))
y=str(input("Enter distance value: "))
z=check_input(x,y)
if(z == True):
    print("Result : ",encryption(x,y),'\n')
    a=str(input("Enter phrase to Decrypt (lowercase, no spaces): "))
    b=str(input("Enter distance value: "))
    print("Result : ",decryption(a,b),'\n')
else:
    print("Wrong Input ..  input in lowercase ..!!")
