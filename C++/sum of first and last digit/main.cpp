#include <iostream>

using namespace std;

int digitnumber(int n)
{
    int g;
    int h;
    int k;
    g = n % 10;
    while(n >= 10){
          n =  n / 10;}
{
        cout<<"So Sum of First and Last Digit of Input Number is = " << g + n <<endl;
    }
}






int main()
{
    int x;
    int y;
    cout <<"Enter a number = " ;
    cin>>x;
    y=digitnumber(x);
}
