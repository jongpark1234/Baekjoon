#include <iostream>
#define MOD 1000000007
using namespace std;
long long power(long long x, long long y) {
	long long r = 1;
	while (y) {
		if (y & 1) r = (r * x) % MOD;
		y >>= 1;
		x = x * x % MOD;
	}
	return r;
}
int main() {
	long long result = 0, mate = 1, n, k, bracket, temp;
	cin >> n >> k;
	bracket = n / 2 - (n & 1 ? 0 : 1);
	result = k * power(k + 1, bracket * 2) % MOD;
	for (long long i = 1; i < bracket + 1; i++) {
		temp = power(k + 1, bracket * 2 - i * 2) * power(k, i) % MOD * mate % MOD;
		mate = mate * (i * 4 + 2) % MOD * power(i + 2, MOD - 2) % MOD;
		result -= temp;
		result %= MOD;
	}
	if (n % 2 == 0) {
		result *= k + 1;
		result %= MOD;
	}
	cout << (result + MOD) % MOD;
}
