import nltk
from math import log10
from math import sqrt

tokens_of_query     = []
query_word_count    = []

q1_freq = []
q2_freq = []
query_ni= []
query_max_freq=[]
query_term_frequency=[]
query_tf_1=[]
query_tf_2=[]

query_idf_1=[]
query_idf_2=[]

new_query_tf_1=[]
new_query_tf_2=[]

length=[]

list_to_compare = []

##Calculate -> Tokens Of Query
def token_of_query(x):
    tokens = nltk.word_tokenize(x)
    for i in tokens:
        tokens_of_query.append(i)


def query_freq(tokens_of_query,freq_list,x):
    for i in tokens_of_query:
        count = 0
        tokens = nltk.word_tokenize(x)
        for j in tokens:
            if(i == j):
                count = count +1
        freq_list.append(count)

def count_ni_list(x):
    count = 0
    for i in x:
        if(i > 0):
            count = count +1
    return count


def calculate_query_ni(q1_freq,q2_freq):
    for i,j in zip(q1_freq,q2_freq):
        check = []
        check.append(i)
        check.append(j)
        x=count_ni_list(check)
        query_ni.append(x)
    
    
    
def calculate_query_freq(x):
    a = (max(x))
    query_max_freq.append(a)


def append_query_freq_to_query_term_frequency(q1_freq,q2_freq):
    query_term_frequency.append(q1_freq)
    query_term_frequency.append(q2_freq)

    
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

def calculate_query_idf(query_ni,query_idf):
    for i in query_ni:
        query_idf.append(log10(2/i))


def calculate_query_tf_idf(query_tf_1,query_tf_2,query_idf):
    for i,j in zip(query_tf_1,query_idf):
        new_query_tf_1.append(round(i*j,2))
    for k,l in zip(query_tf_2,query_idf):
        new_query_tf_2.append(round(k*l,2))    
    

#=> Calculate DotProduct
def dot_product(x,y):

   a= sum(i[0] * i[1] for i in zip(x, x))
   b= sqrt(a)
   c= round(b,2)
   y.append(b)

x= "information relevant contain webpage information"
y= "Sample Dummy data contain relevant"

token_of_query(x)
token_of_query(y)

tokens_of_query_1 = list(dict.fromkeys(tokens_of_query))
query_freq(tokens_of_query_1,q1_freq,x)
query_freq(tokens_of_query_1,q2_freq,y)


calculate_query_ni(q1_freq,q2_freq)

calculate_query_freq(q1_freq)
calculate_query_freq(q2_freq)

print('{:30s}     --->  {:2s}   {:2s}   {:2s}'.format("Terms","Q1","Q2","Ni"))
for i,j,k,l in zip(tokens_of_query_1,q1_freq,q2_freq,query_ni):
    print('{:30s}     --->  {:2d}   {:2d}   {:2d}'.format(i,j,k,l))

print('{:30s}            {:3s}  {:3s}'.format("","-","-"))
print('{:30s}     --->  {:2d}   {:2d}'.format("Maximum Frequency",*query_max_freq))


append_query_freq_to_query_term_frequency(q1_freq,q2_freq)
#print(query_term_frequency)

calculate_query_tf(query_max_freq,query_term_frequency)

print("")
print('{:30s}     --->  {:2s}       {:2s}     {:2s}'.format("Terms","Q1","Q2","Ni"))
print("")
for i,j,k,l in zip(tokens_of_query_1,query_tf_1,query_tf_2,query_ni):
    #print(i,*j,*k)
    print('{:30s}     --->  {:2.2f}    {:2.2f}   {:2d}'.format(i,j,k,l))
    
calculate_query_idf(query_ni,query_idf_1) 
print(query_idf_1)

print("")
print('{:30s}     --->  {:2s}       {:2s}     {:2s}     {:2s}'.format("Terms","Q1","Q2","Ni","IDF"))
print("")
for i,j,k,l,m in zip(tokens_of_query_1,query_tf_1,query_tf_2,query_ni,query_idf_1):
    #print(i,*j,*k)
    print('{:30s}     --->  {:2.2f}    {:2.2f}   {:2d}      {:2.2f}'.format(i,j,k,l,m))

calculate_query_tf_idf(query_tf_1,query_tf_2,query_idf_1)


print("")
print('{:30s}     --->  {:2s}       {:2s}     {:2s}     {:2s}'.format("Terms","Q1","Q2","Ni","IDF"))
print("")
for i,j,k,l,m in zip(tokens_of_query_1,new_query_tf_1,new_query_tf_2,query_ni,query_idf_1):
    #print(i,*j,*k)
    print('{:30s}     --->  {:2.2f}    {:2.2f}   {:2d}      {:2.2f}'.format(i,j,k,l,m))


dot_product(new_query_tf_1,length)
dot_product(new_query_tf_2,length)

#print(length)



elements_list_to_compare = []
for i in range(0,len(q1_freq)):
    if(q1_freq[i] > 0):
        check = []
        check.append(tokens_of_query_1[i])
        check.append(q1_freq[i])
        elements_list_to_compare.append(check)

print(elements_list_to_compare)       


