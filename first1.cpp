#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,n1,n2,n3;
    int count=0;
    cout<<"enter the number";
    cin>>n;
    if(n<0){
        cout<<"enter the valid number";
    }
    if(n>0){
     n1=0;
     n2=1;
     while (count<n)
     {
         /* code */
         cout<<n1<<" ";
         n3=n1+n2;
         n1=n2;
         n2=n3;
         count+=1;

     }
     

    }
}