/*
   Name=M.ROHAN FAROOQUI
   Roll no# p17-6152
   Section A
   Task:Design a class to perform various matrix operations
*/


#include <iostream>
using namespace std;
class matrixType
{
public:
     int matrix[5][6];

public :
      matrixType(){
      }
      void setData(int a[5][6]){
        for(int i=0; i < 5 ; i++)
         for(int j=0 ; j < 6 ; j++){
            matrix[i][j] = a[i][j];}
      }
      void Display(){
        for(int i=0; i < 5 ; i++){
          for(int j=0 ; j < 6 ; j++){
             cout<< matrix[i][j];
             cout<<"  ";}
             cout<< "  "<<endl;}
      }
      matrixType operator +(matrixType d1){
        matrixType b;
        int a[5][6];
        for (int i=0; i< 5; i++){
            for (int j=0; j< 6; j++)
            {
                b.matrix[i][j]= matrix[i][j]+ d1.matrix[i][j];
            }}
        cout<<" " <<endl;
        cout<<"Addition of First & Second matrix :" <<endl;
        for(int i=0; i < 5 ; i++){
          for(int j=0 ; j < 6 ; j++){
            a[i][j];
           // cout<<"  ";}
            return b;}
      }}
      matrixType operator -(matrixType d1){
        matrixType b;
        int a[5][6];
        for (int i=0; i< 5; i++){
            for (int j=0; j< 6; j++)
            {
                b.matrix[i][j]= matrix[i][j] - d1.matrix[i][j];
            }}
        cout<<" " <<endl;
        cout<<"Subtraction of First & Second matrix :" <<endl;
        for(int i=0; i < 5 ; i++){
          for(int j=0 ; j < 6 ; j++){
            a[i][j];
           // cout<<"  ";}
            return b;}
      }}
      matrixType operator *=(matrixType d1){
        matrixType b;
        int a[5][6];
        for (int i=0; i< 5; i++){
            for (int j=0; j< 6; j++)
                for(int k=0; k< 6; k++)
            {
                b.matrix[i][j] = matrix[i][k] * d1.matrix[k][j];
            }}
        cout<<" " <<endl;
        cout<<"Multiplication of First & Second matrix :" <<endl;
        cout << endl << "Output Matrix: " << endl;
        for(int i = 0; i < 5; ++i)
            for(int j = 0; j < 6; ++j){
                   cout << " " << a[i][j];
                   if(j == 6-1)
                   cout << endl;}
        /*for(int i=0; i < 5 ; i++){
          for(int j=0 ; j < 6 ; j++){
            a[i][j];
           // cout<<"  ";}*/
            return b;}
      //}}
};


int main()
{
   matrixType d,d1,d2;
   int a[5][6]={{11,12,13,14,15,16},{17,18,19,10,11,12},{13,14,15,16,17,18},{19,20,21,22,23,24},{25,26,27,28,29,30}};
   int b[5][6]={{1,2,3,4,5,6},{7,8,9,0,1,1},{3,4,5,6,7,8},{9,0,1,2,3,4},{5,6,7,8,9,0}};
   cout<< "First Matrix :" <<endl;
   d.setData(a);
   d.Display();
   cout<< " " <<endl;
   cout<< "Second Matrix :" <<endl;
   d1.setData(b);
   d1.Display();
   //Result:::::addition
   d2 = d + d1;
   d2.Display();
   //Result:::::Subtraction
   d2 = d - d1;
   d2.Display();
   //Result:::::Multiplication
    d *= d1;
   d.Display();


}


