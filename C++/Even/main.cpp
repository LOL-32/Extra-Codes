#include <iostream>

using namespace std;



int even(int x)
{
 if(x % 2 == 0)
 {
  cout<<"Number is Even"<<endl;
 }
 else
 {
  cout<<"Number is Not Even"<<endl;
 }

}
int main()
{
    int x;
    cout<<"Enter a  number = ";
    cin>>x;
    even(x);
}
