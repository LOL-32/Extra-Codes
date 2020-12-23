from bs4 import BeautifulSoup, SoupStrainer
from b import word_list
import nltk





x="This is a boy."


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


l=""
for i in x:
    if i not in punctuations:
        l = l + i

k = l.split()

print(k)



        





















'''query_match =[]
summ = []
ans = []
a= [['information', 2], ['relevant', 1], ['contain', 1], ['webpage', 1]]
for i in word_list:
  for j in i:
     for k in a:
      if(j == k[0]):
          check=[]
          for l in range(1,len(i)):
              f=(i[l]*k[1])
              check.append(f)
          check.insert(0,i[0])
          query_match.append(check)
          
         



for i in query_match:
    check =[]
    for j in range(1,len(i)):
        check.append(i[j])
    summ.append(check)



for i in zip(*summ):
    ans.append(sum(i))




print(query_match)
print(summ)
print(ans)'''
