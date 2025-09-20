#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin>>n;
        ll ans=1e18;
        ll l=0,r=1e10;
        bool f=false;
        while(l<=r){
            ll mid=l+(r-l)/2;
            ll cur=(1LL * mid*(mid-1))/2;
            if(cur>=n){
                ans=min(ans,mid),r=mid-1;
                if(cur==n){
                    f=true;
                    break;
                }

            }
            else l=mid+1;
        }
        if(f)cout<<ans<<'\n';
        else{
            ans--;
            ll cur=(1LL * ans*(ans-1))/2;
            cout<<ans+(n-cur)<<'\n';
        }


    }
    return 0;
}