def average(x):
    sum = 0
    for i in x:
        a= float(i.strip())
        sum = sum + a
    b = sum/len(x)
    return b


def find_string(x):
    l=[]
    with open(x,'r') as f:
        for i in f:
            a = i.strip()
            b = a.split(":")
            if(b[0] == 'X-DSPAM-Confidence'):
                l.append(b[1])
    return l


x = str(input("Enter File Name : "))
y = find_string(x)
z = average(y)
print("\nAverage spam confidence: ",z)


