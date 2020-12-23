#include <iostream>

using namespace std;
//////////////////////////////////////////////Q6 prime number or not /////////////////////////
int main()
{
    int x;
    int count=0;
    cout<< "Enter a number = " <<endl;
    cin>>x;
    if (x < 2){
        cout<<"The entered number is not  Prime" <<endl;
    }
    else{
    for(int i=2;i < x; i++){
        if(x % i ==0){
            count++;
            break;}
    }
    if(count==0)
    {
        cout<<"This entered number is Prime"<<endl;
    }
    else
    {
        cout<<"The entered number is not Prime"<<endl;
    }
}
}

