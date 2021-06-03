def longest_substring(s):
    i = 0
    increase = 0
    longest = 1
    longest_end = 1
    for i in range(len(s)):
            if i < len(s)-1 and s[i+1] >= s[i]:
               increase += 1
            else:
                if increase > longest:
                   longest = increase
                   longest_end = i
                increase = 0
    return  s[longest_end-longest:longest_end+1]

def string_of_numbers(x):
    ans = ""
    for i in x:
        ans = ans + str(i)
    return ans

def average(x):
    summ  = 0
    count = 0
    for i in x:
        summ = summ + int(i)
        count = count + 1
    return summ/count
    

    
def question_1(x):
    l=[]
    for i in x:
        if(i.isdigit()):
            l.append(int(i))
    ans_1 = string_of_numbers(l)
    ans_2 = longest_substring(ans_1)
    ans_3 = round(average(ans_2),3)
    print("String of numbers : ",ans_1 )
    print("Longest substring in numeric descending order is : ",ans_2)
    print("Average : ",ans_3,'\n')
    

x=str(input("Enter Input : "))
question_1(x)

#question_1('56aaww1984sktr235270aYmn145ss785fsq31D0')
#question_1('14erq72lkm79')
