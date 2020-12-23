#include <iostream>

using namespace std;

int sumofalldigits(int n)
{
    cout<<"Digits are = " <<endl;
    int g=0;
    int h=0;
    int i=0;
    while(n>0){
      g = n % 10;
      n = n / 10;
      i++;
      cout<< g <<endl;
    }

}




int main()
{
    int z;
    int x;
    cout<<"Enter a number = " ;
    cin>>x;
    z=sumofalldigits(x);

}



