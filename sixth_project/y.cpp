#include<iostream>
using namespace std;

int main()
{
    int n;
    long long fact =1;
    cout<<"Enter a number:";
    cin>>n;

    if(n<0)
    {
        cout<<"Factorial is not defined for negative numbers."<<endl;
    }
    else
    for(int i=1;i<=n;i++)
    {
        fact=fact*i;
    }
    cout<<"Factriol of "<< n <<  " is:" << fact<<endl;

    return 0;
}