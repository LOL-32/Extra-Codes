#include <iostream>

using namespace std;
///////////////////////////Q5 Fictorial /////////////////
int main()
{
    int x;
    int f=1;
    cout<<"Enter a  number = " <<endl;
    cin>>x;
    for(int i=1 ; i <= x ; i++){
        f = f * i;
    }
{
    cout<<"The answer is = " << f << endl;
}
}
