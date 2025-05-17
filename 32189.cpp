#include <bits/stdc++.h>
using namespace std;
static int dp[3001][3001];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int ans = 0;
    string s;
    cin >> s;
    int n = s.size();
    for (int i = 1; i <= n; i++){
        for(int j = n-1; j >= 0; j--){
            if (s[i-1] == s[j])
                dp[i][j] = dp[i-1][j+1] + 1;
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j+1]);
        }
    }
    for (int k = 0; k <= n; k++){
        int lcs = dp[k][k];
        ans = max(ans, min(k, n-k) - lcs);
    }
    cout << ans << "\n";
}