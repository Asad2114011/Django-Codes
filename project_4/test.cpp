#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin>>n;
        vector<ll>v(n+1);
        vector<pair<ll,ll>>x,y;
        
        for(ll i=1;i<=n;i++)cin>>v[i];
        ll even=0,odd=0;
        ll total=odd-even;
        for(ll i=1;i<=n;i++){
            if(i&1)odd+=v[i],x.push_back({v[i],i});
            else even+=v[i],y.push_back({v[i],i});
        }
        sort(x.begin(),x.end());
        sort(y.rbegin(),y.rend());
        
        
        
        

    }
    return 0;
}