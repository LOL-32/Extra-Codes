#include <iostream>

using namespace std;


int multiplicationofevendigits(int num)
{
    int digit;
    int nodd;
    int neven;
    while (num> 0){
          digit = num % 10;
    if (digit % 2 == 1){
        nodd++;}
    else neven++;{
        num /= 10;
}
{
    cout<<neven << endl;
    cout<<nodd<<endl;
}
}
}



int main()
{
    int x;
    int y;
    cout <<"Enter a number = ";
    cin>>x;
    y=multiplicationofevendigits(x);
}
