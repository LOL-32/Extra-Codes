'''my_dict ={'doc1.html': 0, 'mainpage.html': 0, 'doc5.html': 0, 'doc4.html': 0, 'doc3.html': 0, 'doc2.html': 0, 'doc7.html': 0, 'doc6.html': 0}

x=str(input("Enter File  Name : "))

#for k,v in my_dict.items():
my_dict[x] = 100

print(my_dict)'''

import re



def in_link(file_name,path):
    in_link = 0
    for i in links:
      if(i != path):
         with open(i,'r') as f:
           data = f.read()
           link = re.findall("href=[\"\'](.*?)[\"\']",data)
           c=link[:5]
           for j in c:
             if(j == file_name):
                   in_link = in_link + 1
    in_links.append(str(in_link))

                
      



def out_link(file_name,path):
    out_link = 0
    with open(file_name,'r') as f:
           data = f.read()
           link = re.findall("href=[\"\'](.*?)[\"\']",data)
           c=link[:5]
           for j in c:
             if(j != file_name):
                   out_link = out_link + 1
    out_links.append(str(out_link))
    



file_name = ['doc1.html', 'mainpage.html', 'doc5.html', 'doc4.html', 'doc3.html', 'doc2.html', 'doc7.html', 'doc6.html']
links = ['C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\doc1.html',
         'C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\mainpage.html',
         'C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\doc5.html',
         'C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\doc4.html',
         'C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\doc3.html',
         'C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\doc2.html',
         'C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\doc7.html',
         'C:\\Users\\M.ROHAN FAROOQUI\\Desktop\\Py - Proj - Crawling\\corpus\\doc6.html']

my_dict = {'doc1.html': 0, 'mainpage.html': 100, 'doc5.html': 0, 'doc4.html': 0, 'doc3.html': 0, 'doc2.html': 0, 'doc7.html': 0, 'doc6.html': 0}
in_links  =[]
out_links =[]
damping_factor = 1 - 0.75





for i,j in zip(file_name,links):
    in_link(i,j)
    out_link(i,j)

print(in_links)
print(out_links)

def final_fun():
  check=[]
  temp = []
  for i,j,k,l in zip(file_name,my_dict.items(),in_links,out_links):
      a=float(j[1])
      b=float(k)
      c=int(l)
      d= damping_factor + a/b + a/c
      e= round(d,3)
      #print('{:10.2f}  {:10.2f}   {:10d}  -->   {:10.2f}'.format(a,b,c,d))
      check.append(e)
      
  for i,j in zip(file_name,check):
      my_dict[i] = j



for i in range(0,20):
    final_fun()
    print("Iteration",i+1, "===> ",my_dict)
    
'''final_fun()
print(my_dict)
print("######################")
final_fun()
print(my_dict)'''






