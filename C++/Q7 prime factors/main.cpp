#include <iostream>

using namespace std;

////////////////////////////////////Q7 prime Factors //////////
int prime(int x)
{
    int count=0;
    if (x < 2){
        return 0;
    }
    else{
    for(int i=2;i < x; i++){
        if(x % i ==0){
            count ++;
            break;}
    }
    if(count==0)
    {
        cout<< x  <<endl;
    }

}
}
int main()
{
    int z;
    int x;
    cout<<"Enter a number"<<endl;
    cin>>x;
    for(int i=1;i++;){
        if(x % i == 0){
             z=(prime(i));
    }
    }

}


