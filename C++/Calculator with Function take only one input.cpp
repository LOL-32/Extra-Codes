#include <iostream>
using namespace std;

#include <sstream>

int calculator(string k)
{
 //Variable Declare
 int length = k.size();
 int value=0;
 string a="";
 string b="";
 char c;
 char d;
 float w=0;
 float x=0;


 for(int i=0; i < length ;i++)
 {
  if(k[i] == '+' || k[i] == '-' || k[i] == '*' || k[i] == '/'){break;}
  else{a=a+k[i];}
 }

 for(int i=0; i < length ;i++)
 {
  if(k[i] == '+' || k[i] == '-' || k[i] == '*' || k[i] == '/'){
     d = k[i];
     value  = i+1;}
 }

 for(int i=value; i <= length ; i++){
  if(k[i] == '\0'){break;}
  else{b=b+k[i];}
 }

 stringstream y(a);
 stringstream z(b);
 y >> w;
 z >> x;

 if(d == '+'){cout<<w+x<<endl;}
 else if(d == '-'){cout<<w-x<<endl;}
 else if(d == '*'){cout<<w*x<<endl;}
 else if(d == '/'){cout<<w/x<<endl;}


}

int main()
{
    //Calculator with Function take only one input
    string a;
    cin>>a;
    calculator(a);
}
