#include <iostream>
using namespace std;
string choice;

int main()

{
   choice="1";
   choice="2";
   choice="3";
   choice="4";
   choice="None";
   cout<<"press 1 for Divide"<<endl;
   cout<<"press 2 for Multiplication"<<endl;
   cout<<"press 3 for Addition"<<endl;
   cout<<"press 4 for Subtract"<<endl;
   cout<<"Enter your choice=";
   cin>>choice;
   int x;
   if (choice == "None"){
    cout<<"No choice is selected :):)!!"<<endl;
    }
   else{
   cout<<"Enter a value x="<<endl;
   cin>>x;
   int y;
   cout<<"Enter a value y="<<endl;
   cin>>y;
   if (choice == "1"){
      int d;
      d = x / y;
      cout<<"So result is="<< d <<endl;
   }
   if (choice == "2"){
    int d;
    d= x * y;
    cout<<"So result is="<< d <<endl;
   }
   if (choice == "3"){
    int d;
    d= x + y;
    cout<<"So result is="<< d <<endl;
   }
   if (choice == "4"){
    int d;
    d= x - y;
    cout<<"So result is="<< d <<endl;
   }

}
}
