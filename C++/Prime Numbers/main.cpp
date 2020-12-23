#include <iostream>

using namespace std;

int prime_numbers(int x)
{

 for(int i=2;i <= x;i++)
 {
  if(x % i == 0)
  {
    x = true;
  }
  else
  {
    x = false;
   }
   if (x = false)
   {
       cout<<"Number is ";
   }
   else
   {
       cout<<"Number not";
   }
}
}




int main()
{
    int x;
    cout<<"Enter a number = ";
    cin>>x;
    prime_numbers(x);

}
