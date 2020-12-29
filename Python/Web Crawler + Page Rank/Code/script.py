############################### IMPORT ###############################
from porter_stemmer import *
from math import log10
from math import sqrt
import codecs
import re
############################### Lists ###############################
##### Pre List #########
crawled             = []
file_links          = []
token_of_all_files  = []
stop_word           = []
port_stemp          = []
stem_words          = []
terms_frequency     = []
n_i                 = []
maximum_freq        = []
tf                  = []
idf                 = []
tf_idf              = []
lengths_of_document = []
##### Post-List ########
tokens_of_query     = []
query_word_count    = []


q1_freq = []
q2_freq = []
query_ni= []
query_max_freq=[]
query_tf=[]
query_term_frequency=[]
query_tf_1=[]
query_tf_2=[]
query_idf=[]
new_query_tf_1=[]
new_query_tf_2=[]

length_of_query=[]

elements_list_to_compare_1 = []
elements_list_to_compare_2 = []

query_match_1 =[]
query_match_2 =[]

summ_1= []
summ_2= []
ans_1 = []
ans_2 = []
page_rank_1 =[]
page_rank_2 =[]
final_1 = []
final_2 =[]
in_links  =[]
out_links =[]
########################### Variables ###############################
count = 0
regex= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
damping_factor = 1 - 0.75
########################### Backend Functions #######################
def in_link(file_name,path):
    in_link = 0
    for i in file_links:
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
    with open(path,'r') as f:
           data = f.read()
           link = re.findall("href=[\"\'](.*?)[\"\']",data)
           c=link[:5]
           for j in c:
             if(j != file_name):
                   out_link = out_link + 1
    out_links.append(str(out_link))
    
def make_list(a):
    with open(a,'r') as f:
      data = f.read()
      links = re.findall("href=[\"\'](.*?)[\"\']",data)
    return links
      


def make_file_links(file_names,path):
    for i in file_names:
        a = path + "\\" + i
        file_links.append(a)


def clean_common_tokens(token_of_all_files,stop_words,port_stemp):
    a=port_stemp
    for  i in token_of_all_files:
      if(i not in stop_words):
            a.append(i)


def check_for_special_c(x):
    for i in x:
        #Special Charachters & Numbers Range => 32–47 / 58–64 / 91–96 / 123–126 /48-57
        a=ord(i)
        if(a >= 32 and a <= 47 or a >= 58 and a <= 64 or a >= 91 and a <= 96 or a >= 123 and a <= 126 or a >= 48 and a <= 57):
            return False
        else:
            return True


def count_ni_list(x):
    count = 0
    for i in x:
        if(i > 0):
            count = count +1
    return count

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


#=> Calculate DotProduct
def dot_product(x,y):
   y = lengths_of_document 
   if len(x) != len(x):
      return 0

   a= sum(i[0] * i[1] for i in zip(x, x))
   b= sqrt(a)
   c= round(b,2)
   y.append(b)

#=> Calculate DotProduct_2
def dot_product_2(x,y):
   a= sum(i[0] * i[1] for i in zip(x, x))
   b= sqrt(a)
   c= round(b,2)
   y.append(b)
def calculate_query_freq(x):
    a = (max(x))
    query_max_freq.append(a)

def append_query_freq_to_query_term_frequency(q1_freq,q2_freq):
    query_term_frequency.append(q1_freq)
    query_term_frequency.append(q2_freq)


def Sort(x): 
    l = len(x) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (x[j][1] > x[j + 1][1]): 
                temp = x[j] 
                x[j]= x[j + 1] 
                x[j + 1]= temp
    return x


def tokenize(x):
    l=""
    for i in x:
        if i not in punctuations:
            l = l + i
    k = l.split()
    return k

        
########################### Main Functions ##########################

##
def query_solve(terms_frequency,elements_list_to_compare,query_match):
    d= query_match
    for i in terms_frequency:
      for j in i:
         for k in elements_list_to_compare:
          if(j == k[0]):
              check=[]
              for l in range(1,len(i)):
                  f=(i[l]*k[1])
                  check.append(f)
              check.insert(0,i[0])
              d.append(check)    


##Get list of words to compare
def list_to_compare(q1_freq,elements_list_to_compare):
    d=elements_list_to_compare
    for i in range(0,len(q1_freq)):
        if(q1_freq[i] > 0):
            check = []
            check.append(tokens_of_query_1[i])
            check.append(q1_freq[i])
            d.append(check)

##Calculate -> TF.IDF Query
def calculate_query_tf_idf(query_tf_1,query_tf_2,query_idf):
    for i,j in zip(query_tf_1,query_idf):
        new_query_tf_1.append(round(i*j,2))
    for k,l in zip(query_tf_2,query_idf):
        new_query_tf_2.append(round(k*l,2))    

##Calculate -> IDF of Query
def calculate_query_idf(query_ni):
    for i in query_ni:
        query_idf.append(log10(2/i))
    
##Calculate -> TF of Query
def calculate_query_tf(query_max_freq,query_term_frequency):
    a=query_max_freq[0]
    b=query_max_freq[1]

    c=query_term_frequency[0]
    d=query_term_frequency[1]
    ans_1 = [x / a for x in c]
    ans_2 = [x / b for x in d]
    for i in ans_1:
        query_tf_1.append(i)
    for j in ans_2:
        query_tf_2.append(j)    

    
##Calculate -> Max of Query
def calculate_query_freq(x):
    a = max(x)
    query_max_freq.append(a)
    
##Calculate -> NI of Query
def calculate_query_ni(q1_freq,q2_freq):
    for i,j in zip(q1_freq,q2_freq):
        check = []
        check.append(i)
        check.append(j)
        x=count_ni_list(check)
        query_ni.append(x)

##Calculate -> Frequency of Query
def query_freq(tokens_of_query,freq_list,x):
    for i in tokens_of_query:
        count = 0
        #tokens = nltk.word_tokenize(x)
        tokens = tokenize(x)
        for j in tokens:
            if(i == j):
                count = count +1
        freq_list.append(count)


##Calculate -> Tokens of Query 
def token_of_query(x,stop_word):
    #tokens = nltk.word_tokenize(x)
    tokens = tokenize(x)
    for i in tokens:
      if(i not in stop_word):
            tokens_of_query.append(i)

##Calculate -> Length    
def length(tf_idf,stem_words,crawled,lengths_of_document):
  for i in range(0,len(crawled)):
    check   = []
    check_1 = []
    count = 0 
    for j in tf_idf:
        count = count +1 
        check.append(j[i+1])
        if(count == len(stem_words)):
            dot_product(check,lengths_of_document)

##Calculate -> TF_IDF
def calculate_tf_idf(tf,idf,tf_idf):
    d = tf_idf
    count = 0
    for i in tf:
        check=[]
        for j in range(1,len(i)):
           a = i[j]*idf[count]
           #b = normal_round(a)
           b = round(a,2)
           check.append(b)
        check.insert(0,i[0])
        d.append(check)
        count = count + 1
        
##Calculate -> IDF
def calculate_idf(total_doc,n_i,idf):
    d=n_i
    e=idf
    for i in d:
        try:
            a= total_doc/i
            b=log10(a)
            e.append(b)
        except ZeroDivisionError:
            c=0
            e.append(c)

##Calculate -> TF 
def calculate_tf(terms_frequency,maximum_freq,tf):
    d= tf
    for i in terms_frequency:
        check=[]
        for j in range(1,len(i)):
           try:
            a = i[j] / maximum_freq[j-1]
            b = round(a,1)
            check.append(b)
           except:
            b=0   
            check.append(b)               
        check.insert(0,i[0])
        d.append(check)
        print('{:50s}     --->  {:10.1f}  {:10.1f}  {:10.1f}  {:10.1f}  {:10.1f}  {:10.1f}  {:10.1f}  {:10.1f}'.format(*check))


##Maximum Frequency
def max_freq(crawled,terms_frequency,maximum_freq):
    a= maximum_freq
    for i in range(0,len(crawled)):
        check = []
        for j in terms_frequency :
            check.append(j[i+1])
        a.append(max(check))


##Calculate -> NI
def calculate_ni(word_list,file_links,terms_frequency,ni):
    e =terms_frequency
    z = ni
    for i in word_list:
     c=[]
     for j in file_links:   
        count = 0
        countt= 0
        b=""
        a=[]
        with codecs.open(j,'r') as f: 
             data = f.read()
             clean = re.compile('<.*?>')
             text = re.sub(clean, '', data)
             tokens = tokenize(text)
        for k in tokens:
            if(check_for_special_c(k) == True):
                if(i == k):
                    count = count + 1
        c.append(count)
     d = count_ni_list(c)
     print('{:50s}     --->  {:9d}   {:9d}   {:9d}   {:9d}   {:9d}   {:9d}   {:9d}   {:9d}         ==>    {:9d}'.format(i,c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],d))
     z.append(d)
     c.insert(0,i)
     e.append(c)
     
    


##Get -> Stopwords
def stop_words(word_list,file_links,stop_word):
    d=stop_word
    c=[]
    for i in word_list:
     count = 0
     for j in file_links:
         b=""
         a=[]
         with codecs.open(j,'r',encoding='utf-8') as f: 
            data = f.read()
            clean = re.compile('<.*?>')
            text = re.sub(clean, '', data)
            #tokens = nltk.word_tokenize(b)
            tokens = tokenize(text)    
         if(i in tokens):
            count = count + 1
     if(count == len(file_links)):
         d.append(i)  
         

##Tokenziation : Get Tokens of All Html Files
def tokenization(link):
    #token = []
    string=""
    with codecs.open(link,'r',encoding='utf-8') as f:
       data = f.read()
       clean = re.compile('<.*?>')
       text = re.sub(clean, '', data)
       tokens = tokenize(text)
       for i in tokens: 
           if(len(i) > 1 and i not in token_of_all_files):
                token_of_all_files.append(i)



## Crawling : It will Crawl in Every Webpage and Give you Html Links in Every Page , Move from One apge to other automatically 
def crawler(path,file_name,links):
    global count 
    with open(links,'r') as f:   
      data = f.read()
      links = re.findall("href=[\"\'](.*?)[\"\']",data)
      c=links[:5]
      for i in c:
          if(i not in crawled):
              print("")
              print("####################### Now Crawling for links in webpage : "+ i+" #######################")
              print("")
              d= path + "\\" + i
              e= make_list(d)
              if(c not in crawled):
                  count = count + 1
                  crawled.append(i)
                  for i in e:
                      print("---> ",i)
                      tokenization(path+"\\"+i)
              for k in e:
                  if(k  not in crawled):
                      crawler(path,k,d)
         
                
                
                  

############################### Scrit Starts #########################

path = str(input("Enter file path without name and extension : "))
file_name = str(input("Enter Page name and extension to strat crawling : "))
link = path+"\\"+file_name

print("")
print("")
print("#######################                 Crawler starts             #######################")
crawler(path,file_name,link)
print("")
print("")
print("#######################                  Ending Crawler            #######################")
print("")
print("")

print("#######################                   Stop Words                #######################")
print("")

make_file_links(crawled,path)
stop_words(token_of_all_files,file_links,stop_word)
for  i in stop_word :
    print("==> ",i)


print("")
print("#######################                   Porter Stemmer            #######################")
print("")

clean_common_tokens(token_of_all_files,stop_word,port_stemp)

p = PorterStemmer()
for w in port_stemp:
    if(check_for_special_c(w) == True):
        stem_words.append(w)
        print('{:50s}      --->  {}'.format(w, p.stem(w,0,len(w)-1)))


print("")
print("#######################               NI of Terms Documents         #######################")
print("")

print('{:50s}     --->  {:9s}   {:9s}   {:9s}   {:9s}   {:9s}   {:9s}   {:9s}   {:9s}                   {:9s}'.format("Terms",*crawled,"N_i"))
calculate_ni(stem_words,file_links,terms_frequency,n_i)

print("")
print("#######################      Maximum Words Frequency in Documents    #######################")
print("")

max_freq(crawled,terms_frequency,maximum_freq)
print('{:50s}     --->  {:9d}   {:9d}   {:9d}   {:9d}   {:9d}   {:9d}   {:9d}   {:9d}'.format("Maximum Frequency",*maximum_freq))

print("")
print("#######################                          TF                  #######################")
print("")

calculate_tf(terms_frequency,maximum_freq,tf)


print("")
print("#######################                          IDF                 #######################")
print("")
     
calculate_idf(len(crawled),n_i,idf)
print('{:50s}     --->     {:9s}   {:9s}   {:9s}   {:9s}   {:9s}   {:9s}   {:9s}    {:9s}         {:9s}  {:9s}'.format("Terms",*crawled,"N_i","IDF"))
print("")
for  i,j,k in zip(tf,n_i,idf):
    print('{:50s}     --->  {:10.2f}   {:10.1f}   {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}   {:9d}   {:10.2f}'.format(*i,j,k))

    

print("")
print("#######################                        TF.IDF                #######################")
print("")

calculate_tf_idf(tf,idf,tf_idf)



print('{:50s}     --->     {:9s}   {:9s}   {:9s}   {:9s}   {:9s}   {:9s}   {:9s}    {:9s}'.format("Terms",*crawled))
for i in tf_idf:
    print('{:50s}     --->  {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}   {:10.2f}'.format(*i))


print("")
print("#######################                  Page -Weight / LENGTH        #######################")
print("")

length(tf_idf,stem_words,crawled,lengths_of_document)
print('{:50s}     --->  {:10.2f}   {:10.2f}   {:10.2f}  {:10.2f}  {:10.2f}  {:10.2f}  {:10.2f}  {:10.2f}'.format("Length",*lengths_of_document))

############################################################# PART - 2   #########################################################

print("")
print("#######################                        Queries                #######################")
print("")


x=str(input("Enter a Query 1: "))
y=str(input("Enter a Query 2: "))


#x= "information relevant contain webpage information"
#y= "Sample Dummy data contain relevant"

token_of_query(x,stop_word)
token_of_query(y,stop_word)

tokens_of_query_1 = list(dict.fromkeys(tokens_of_query))
query_freq(tokens_of_query_1,q1_freq,x)
query_freq(tokens_of_query_1,q2_freq,y)


print("")
print("#######################                    Frequency of Query         #######################")
print("")
calculate_query_ni(q1_freq,q2_freq)
print('{:30s}     --->  {:2s}   {:2s}   {:2s}'.format("Terms","Q1","Q2","Ni"))
for i,j,k,l in zip(tokens_of_query_1,q1_freq,q2_freq,query_ni):
    print('{:30s}     --->  {:2d}   {:2d}   {:2d}'.format(i,j,k,l))


print("")
print("#######################      Maximum Words Frequency      #######################")
print("")

calculate_query_freq(q1_freq)
calculate_query_freq(q2_freq)

print('{:30s}     --->  {:2d}   {:2d}'.format("Maximum Frequency",*query_max_freq))

print("")
print("#######################                          TF                  #######################")
print("")

append_query_freq_to_query_term_frequency(q1_freq,q2_freq)
calculate_query_tf(query_max_freq,query_term_frequency)

print("")
print('{:30s}     --->  {:2s}       {:2s}     {:2s}'.format("Terms","Q1","Q2","Ni"))
print("")
for i,j,k,l in zip(tokens_of_query_1,query_tf_1,query_tf_2,query_ni):
    print('{:30s}     --->  {:2.2f}    {:2.2f}   {:2d}'.format(i,j,k,l))
    

print("")
print("#######################                          IDF                 #######################")
print("")

calculate_query_idf(query_ni)  
print('{:30s}     --->  {:2s}       {:2s}     {:2s}     {:2s}'.format("Terms","Q1","Q2","Ni","IDF"))
print("")
for i,j,k,l,m in zip(tokens_of_query_1,query_tf_1,query_tf_2,query_ni,query_idf):
    print('{:30s}     --->  {:2.2f}    {:2.2f}   {:2d}      {:2.2f}'.format(i,j,k,l,m))


print("")
print("#######################                          TF.IDF              #######################")
print("")
calculate_query_tf_idf(query_tf_1,query_tf_2,query_idf)
print('{:30s}     --->  {:2s}       {:2s}     {:2s}     {:2s}'.format("Terms","Q1","Q2","Ni","IDF"))
print("")
for i,j,k,l,m in zip(tokens_of_query_1,new_query_tf_1,new_query_tf_2,query_ni,query_idf):
    print('{:30s}     --->  {:2.2f}    {:2.2f}   {:2d}      {:2.2f}'.format(i,j,k,l,m))

print("")
print("#######################                  Query-Weight / LENGTH        #######################")
print("")

dot_product_2(new_query_tf_1,length_of_query)
dot_product_2(new_query_tf_2,length_of_query)
print('{:30s}     --->  {:2.2f}    {:2.2f}   '.format("Length",*length_of_query))
print("")

list_to_compare(q1_freq,elements_list_to_compare_1)
list_to_compare(q2_freq,elements_list_to_compare_2)

query_solve(terms_frequency,elements_list_to_compare_1,query_match_1)
query_solve(terms_frequency,elements_list_to_compare_2,query_match_2)

for i in query_match_1:
    check =[]
    for j in range(1,len(i)):
        check.append(i[j])
    summ_1.append(check)

for i in query_match_2:
    check =[]
    for j in range(1,len(i)):
        check.append(i[j])
    summ_2.append(check)


for i in zip(*summ_1):
    ans_1.append(sum(i))

for i in zip(*summ_2):
    ans_2.append(sum(i))

for i,j in zip(ans_1,lengths_of_document):
    try:
        a=i/(sqrt(pow(j,2)) * sqrt(pow(query_max_freq[0],2)))
        page_rank_1.append(a)
    except:
        page_rank_1.append(0)


for i,j in zip(ans_2,lengths_of_document):
    try:
        a=i/(sqrt(pow(j,2)) * sqrt(pow(query_max_freq[0],2)))
        page_rank_2.append(a)
    except:
        page_rank_2.append(0)


for i,j in zip(crawled,page_rank_1):
    check =[]
    check.append(i)
    check.append(j)
    final_1.append(check)



for i,j in zip(crawled,page_rank_2):
    check =[]
    check.append(i)
    check.append(j)
    final_2.append(check)

    
print("")
print("#######################                  Page - Rank-1           #######################")
print("")
x=Sort(final_1)
num = len(x)-1
count = 1
for i in range(num,-1,-1):
    print('{:30s}  => {:2d}  {:30s}  {:30s}  {:30s}  {:10.2f}'.format("Rank",count," Doc Name => ",x[i][0]," Value => ",x[i][1]))
    count = count + 1


print("")
print("#######################                  Page - Rank-2          #######################")
print("")
x=Sort(final_2)
num = len(x)-1
count = 1
for i in range(num,-1,-1):
    print('{:30s}  => {:2d}  {:30s}  {:30s}  {:30s}  {:10.2f}'.format("Rank",count," Doc Name => ",x[i][0]," Value => ",x[i][1]))
    count = count + 1


print("")
print("###########################################################################################################################################################")
print("")
############################################################# PART - 3   #########################################################
print("")
print("#######################                 File - Names          #######################")
print("")


my_dict={}

for i in range(0,len(crawled)):
    my_dict[crawled[i]] = 0
    print("File ",i+1," ==> ",crawled[i])

def final_fun():
  check=[]
  for i,j,k,l in zip(crawled,my_dict.items(),in_links,out_links):
      a=float(j[1])
      b=float(k)
      c=int(l)
      d= damping_factor + a/b + a/c
      e= round(d,3)
      #print('{:10.2f}  {:10.2f}   {:10d}  -->   {:10.2f}'.format(a,b,c,d))
      check.append(e)
      
  for i,j in zip(crawled,check):
      my_dict[i] = j
      

x=str(input("Enter Webpage Name (from above) : "))
#x="doc6.html"
if(x in crawled):
    my_dict[x] = 100
    print("")
    print("Assign 100 weightage to ",x," Except it all others assign 0")
    print("")
    print(my_dict)
    print("")
    for i,j in zip(crawled,file_links):
        in_link(i,j)
        out_link(i,j)
    print("")
    print("")
    for i in range(0,20):
        final_fun()
        print("")
        print("Iteration",i+1, "===> ",my_dict)
       
    print("")
    print("")
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    lot = 1
    for i in sorted_dict:
        print('{:5s} > {:2d} ==> {:10s} > {:20s} ==> {:10s} > {:10.3f}'.format(" Rank ",lot," Page Name ",i[0]," Value ", i[1]))
        lot = lot + 1
    
    


    
