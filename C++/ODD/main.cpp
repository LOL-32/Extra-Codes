#include <iostream>
using namespace std;



int odd(int x)
{
  if(x % 2 == 0)
  {
      cout<<"Number is Not ODD Number"<<endl;
  }
  else
  {
      cout<<"Number is ODD Number"<<endl;
  }
}
int main()
{
    int x;
    cout << "Enter a number";
    cin>>x;
    odd(x);
}
