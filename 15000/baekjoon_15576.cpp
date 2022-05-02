#include <cstdio>
#include <cmath>
#include <vector>
#include <complex>
#include <algorithm>
using namespace std;
const double PI = acos(-1);
typedef complex<double> base;
void FFT(vector<base> &f, bool inv) {
	int n = f.size();
	for (int i = 1, j = 0; i < n; i++){
		int b = n / 2;
		while (!((j ^= b) & b)) {
			b /= 2;
		}
		if (i < j) {
			swap(f[i], f[j]);
		}
	}
	for (int k = 1; k < n; k *= 2) {
		double a = (inv ? PI / k : -PI / k);
		base w(cos(a), sin(a));
		for (int i = 0; i < n; i += k * 2) {
			base wp(1, 0);
			for (int j = 0; j < k; j++) {
				base x = f[i + j], y = f[i + j + k] * wp;
				f[i + j] = x + y;
				f[i + j + k] = x - y;
				wp *= w;
			}
		}
	}
	if (inv) {
		for (int i = 0; i < n; i++) {
			f[i] /= n;
		}
	}
}
void multiply(vector<base> a, vector<base> b, vector<base> &c){
	int n = 1;
	while (n < a.size() + 1 || n < b.size() + 1) {
		n *= 2;
	}
	n *= 2;
	a.resize(n);
	b.resize(n);
	c.resize(n);
	FFT(a, false);
	FFT(b, false);
	for(int i = 0; i < n; i++) {
		c[i] = a[i] * b[i];
	}
	FFT(c, true);
}

int main(){
	vector<base> A, B, C;
	while (true) {
		char c = getchar();
		if (c == ' ') {
			break;
		}
		A.push_back(base(c - '0', 0));
	}
	while (true) {
		char c = getchar();
		if (c == '\n') {
			break;
		}
		B.push_back(base(c - '0', 0));
	}
	reverse(A.begin(), A.end());
	reverse(B.begin(), B.end());
	multiply(A, B, C);
	int carry = 0, i;
	vector<int> R;
	for (i = 0; i < C.size(); i++){
		int temp = (int)round(C[i].real()) + carry;
		R.push_back(temp % 10);
		carry = temp / 10;
	}
	while (carry > 0) {
		R.push_back(carry % 10);
		carry /= 10;
	}
	for (i = R.size() - 1; i >= 0 && R[i] == 0; i--);
	if (i < 0) {
		puts("0");
	}
	else {
		for(; i >= 0; i--) {
			putchar(R[i] + '0');
		}
	}
}
