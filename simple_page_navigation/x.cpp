#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin>>n;
  string s;
  cin>>s;
  vector<int>x;
  for(int i=0;i<2*n;i++){
    if(s[i]=='A')x.push_back(i);
  }
  ll a=0,b=0;
  int j=1;
  for(int i=0;i<x.size();i++){
    ll l=2*i;
    ll r=l+1;
    a+=abs(x[i] -l);
    b+=abs(x[i] -r);
  }
  cout<<min(a,b)<<endl;

    return 0;
}