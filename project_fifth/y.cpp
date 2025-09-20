#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; 
    if (!(cin >> T)) return 0;
    while (T--) {
        int n, k; 
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];

        vector<int> freq(n + 1, 0);
        for (int x : a) ++freq[x];

        bool ok = true;
        for (int v = 1; v <= n; ++v) {
            if (freq[v] % k != 0) { ok = false; break; }
        }
        if (!ok) {
            cout << 0 << '\n';
            continue;
        }

        // compute limits
        vector<int> limit(n + 1, 0);
        for (int v = 1; v <= n; ++v) limit[v] = freq[v] / k;

        vector<int> curr(n + 1, 0);
        ll ans = 0;
        int L = 0;
        for (int R = 0; R < n; ++R) {
            ++curr[a[R]];
            // Only a[R] could newly exceed its limit
            while (curr[a[R]] > limit[a[R]]) {
                --curr[a[L]];
                ++L;
            }
            ans += (R - L + 1);
        }

        cout << ans << '\n';
    }
    return 0;
}
