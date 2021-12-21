# pypy3
from sys import stdin
counter = [
	[906150257, 906150293], [906150295, 906150307], [906150311, 906150313], [906150315, 906151515],
	[906151517, 906151575], [906154583, 906154585], [906154605, 906154605], [906154609, 906154757],
	[906154763, 906154763], [906154769, 906154769], [906154789, 906154789], [906154791, 906154791],
	[906154793, 906154793], [906154825, 906154825], [906154829, 906154829], [906154837, 906154837],
	[906154857, 906154857], [906154865, 906154881], [906154885, 906154885], [906154887, 906154887],
	[906154889, 906154889], [906154891, 906154891], [906154893, 906154893], [906154895, 906154907],
	[906154909, 906154911], [906154915, 906154927], [906154947, 906154949], [906180359, 906180361],
	[906180363, 906180363], [906180365, 906180365], [906180367, 906180369], [906180371, 906180373],
	[906180375, 906180375], [906180391, 906180517], [906180519, 906180519], [906180525, 906180533],
	[906180537, 906180553], [906180555, 906192697], [906192847, 906192865], [906192867, 906192903],
	[906192905, 906192905], [906192907, 906192965], [906192971, 906192971], [906192979, 906192983],
	[906192985, 906193227], [906193229, 906193233], [906193245, 906193245], [906193247, 906193247],
	[906193303, 906193303], [906193419, 906193419], [906193465, 906193465], [906193475, 906193475],
	[906193477, 906193477], [906194931, 906194931], [906194933, 906194945], [906194949, 906194949],
	[906194951, 906194967], [906194979, 906194979], [906195099, 906195099], [906195109, 906195149],
	[906195151, 906195151], [906195297, 906195297], [906195299, 906195985], [906195989, 906195989],
	[906196009, 906196009], [906196011, 906196013], [906196015, 906196015], [906196045, 906196051],
	[906196053, 906196055], [906196057, 906196071], [906196077, 906196079], [906196081, 906196081],
	[906196083, 906196091], [906196099, 906208711], [906208713, 906208713], [906208731, 906208731],
	[906209041, 906209063], [906209067, 906209067], [906209069, 906209069], [906209071, 906209223],
	[906209227, 906209227], [906209233, 906209235], [906209237, 906209237], [906209241, 906209241],
	[906209243, 906209271], [906209283, 906209283], [906209285, 906477701], [906477735, 906477811],
	[906477867, 906477867], [906477869, 906477869], [906477871, 906477899], [906477901, 906477901],
	[906477903, 906477905], [906477929, 906477931], [906477933, 906477933], [906477935, 906477935],
	[906477937, 906486639], [906486805, 906486805], [906486807, 906486807], [906486817, 906486817],
	[906486819, 906486819], [906486821, 906486831], [906486843, 906486853], [906486855, 906486855],
	[906486909, 906486913], [906486917, 906486973], [906486975, 906487001], [906487005, 906487063],
	[906487065, 906487065], [906487069, 906487069], [906487071, 906487071], [906487073, 906487077],
	[906487085, 906487085], [906487087, 906487101], [906487185, 906487185], [906487187, 906487189],
	[906487191, 906487191], [906487193, 906487193], [906487195, 906487203], [906487205, 906487205],
	[906487259, 906487259], [906487261, 906487261], [906487263, 906487263], [906487271, 906487287],
	[906487933, 906487933], [906487937, 906487937], [906487949, 906487973], [906487975, 906487993],
	[906487995, 906488001], [906488003, 906488003], [906488007, 906488007], [906488009, 906488009],
	[906488023, 906488025], [906488027, 906488065], [906488067, 906488067], [906488077, 906488079]
]
for _ in range(int(stdin.readline())):
    E = False
    n = int(stdin.readline())
    for i in range(136):
        if counter[i][0] <= n <= counter[i][1]:
            E = True 
            break
    if n == 1 or E:
        print('E')
    else:
        print('O')

# 반례 찾는 코드 ( 밀러-라빈, C++ )
# #include <bits/stdc++.h>
# #define fastio ios::sync_with_stdio(0),cin.tie(0),cout.tie(0)
# using namespace std;
# typedef long long ll;
# namespace miller_rabin {
# 	ll mul(ll x,ll y,ll mod) [return x * y % mod;]
# 	ll _pow(ll x,ll y,ll p) {
# 		ll ret = 1,piv = x % p;
# 		while (y) {
# 			if (y & 1) ret = mul(ret,piv,p);
# 			piv = mul(piv,piv,p);
# 			y >>= 1;
# 		}
# 		return ret;
# 	}
# 	bool miller_rabin(ll x,ll a) {
# 		if (x % a == 0) return 0;
# 		ll d = x - 1;
# 		while (1) {
# 			ll tmp = _pow(a,d,x);
# 			if (d & 1) return (tmp != 1 && tmp != x - 1);
# 			else if (tmp == x - 1) return 0;
# 			d >>= 1;
# 		}
# 	}
# 	bool isprime(ll x) {
# 		for (auto& i : [2,3,5,7,11,13,17,19,23,29,31,37]) {
# 			if (x == i) return 1;
# 			if (x > 40 && miller_rabin(x,i)) return 0;
# 		}
# 		if (x <= 40) return 0;
# 		return 1;
# 	}
#}
# namespace pollard_rho {
# 	void rec(ll n,vector<ll>& v) {
# 		if (n == 1) return;
# 		if (n % 2 == 0) {
# 			v.push_back(2);
# 			rec(n / 2,v);
# 			return;
# 		}
# 		if (miller_rabin::isprime(n)) {
# 			v.push_back(n);
# 			return;
# 		}
# 		ll a,b,c,g = n;
# 		auto f = [&](ll x) {
# 			return (c + miller_rabin::mul(x,x,n)) % n;
# 		};
# 		do {
# 			if (g == n) {
# 				a = b = rand() % (n - 2) + 2;
# 				c = rand() % 20 + 1;
# 			}
# 			a = f(a);
# 			b = f(f(b));
# 			g = gcd(abs(a - b),n);
# 		} while (g == 1);
# 		rec(g,v);
# 		rec(n / g,v);
# 	}
# 	vector<ll> factorize(ll n) {
# 		vector<ll> ret;
# 		rec(n,ret);
# 		sort(ret.begin(),ret.end());
# 		return ret;
# 	}
#}
# bool f(ll n) {
# 	auto v = pollard_rho::factorize(n);
# 	return v.size() & 1;
#}
# int main() {
# 	fastio;
# 	int cnt = 0,t = 0;
# 	for (int i = 906150257; i <= 1'000'000'001; i++) {
# 		int prev = cnt;
# 		cnt += f(i) ? 1 : -1;
# 		if (!prev && cnt < 0) cout << "[" << i << ",";
# 		else if (prev < 0 && !cnt) {
# 			cout << i - 1 << "],",t++;
# 			if (t % 4 == 0) cout << '\n';
# 		}
# 	}
#}
