#include<bits/stdc++.h>
#define inf 0x3f3f3f3f
#define test cout<<1<<endl
#define pii pair<int,int>
#define pll pair<int64,int64>
#define epb emplace_back
#define mkp make_pair
#define f_ first
#define s_ second
#define pq priority_queue
using namespace std;
inline int read() {
	int x = 0, f = 1;
	char ch = getchar();
	while (!isdigit(ch)) { if (ch == '-') f = -1; ch = getchar(); }
	while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
	return x * f;
}
const int MOD = 1000000007;
const int mod = 998244353;
#define int64 long long
int64 n, m;
int t;
int k;
string s;
int64 ans;
int len;
bool vis[100005][6];
vector<int64> nums;
vector<int> record;
inline int64 fast_pow(int64 a, int64 b, int m) {
	int64 ret = 1;
	while (b) {
		if (b & 1) {
			ret = ((ret % m) * (a % m)) % m;
		}
		a = ((a % m) * (a % m)) % m;
		b >>= 1;
	}
	return ret;
}
// inline int64 f(int pos, int pre, bool is_num, bool is_limit){
// 	if (pos == len)return is_num;
// 	if (is_num and !is_limit and ~dp[pos][pre])return dp[pos][pre];
// 	int64 ret = 0;
// 	if (!is_num)ret += f(pos + 1, -2, false, false);
// 	for (int start = 1 - is_num, up = is_limit ? s[pos] - '0' : 9; start <= up; start++) {
// 		if (abs(pre - start) >= 2) {
// 			ret += f(pos + 1, start, true, is_limit and start == up);//前每一位都顶着了is_limit为true
// 		}
// 	}
// 	if (!is_limit and !is_num)dp[pos][pre] = ret;	//如果is_limit=true,is_num=true,会影响到前一位的取值范围，所记录的答案是全的
// 	return ret;
// }
int a[100005];
int b[100005];
int up[100005];
int bo[100005];
inline bool dfs(int i) {
	if (i == n) return true;
    for (int j = bo[i];j <= up[i];++j)
    {
        if (i>0)
        {
            if (a[i] == a[i-1] && j == b[i-1]) continue;
            if (a[i] > a[i-1] && j<= b[i-1]) continue;
            if (a[i] < a[i-1] && j>=b[i-1]) break;
        }
        b[i] = j;
        if (dfs(i+1)) return true;
    }
    return false;
}
void solve() {
    if (n == 1)
    {
        cout<<1;
        return;
    }

	for (int i = 0; i < n; i++) {
		cin >> a[i];
        bo[i] = 1;
        up[i] = 5;
	}
    for (int i = 1;i<n;++i)
    {
        int x = a[i-1],y=a[i];
        if (y>x) bo[i] = bo[i-1] + 1;
        else if (y<x) up[i] = up[i-1] - 1;

        if (up[i]<bo[i])
        {
            cout<<-1;
            return ;
        }
    }
    for (int i = n-2;i>=0;--i)
    {
        int x = a[i],y=a[i+1];
        if (x>y) bo[i] = bo[i + 1] + 1;
        else if (x<y) up[i] = up[i + 1] - 1;

        if (up[i]<bo[i])
        {
            cout<<-1;
            return ;
        }
    }
    if (dfs(0)) for (int i = 0;i < n;++i) cout << b[i]<<" ";
    else cout<<-1;


	return;
}
signed main() {
	// n = read();
	// m = read();
	// k = read();
	// t = read();

	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> n;

	solve();

	return 0;
}