#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;
#define MAX 1000000000
int main() {
	long long r, b;
	long double result = 1;
	scanf("%lld %lld", &r, &b);
	if (r > b) {
		swap(r, b);
	}
	if (r < 50001) {
		for (long long i = 1; i <= r; i++) {
			result *= i / (long double)(r + b - i + 1);
		}
		result *= pow(2, r + b);
	}
	else {
		result = sqrt(r * acos(-1)) * (1 + 1 / (long double)(r << 3));
		for (long long i = r; i < b; i++) {
			result *= ((i + 1) << 1) / (long double)(r + i + 1);
			if (result > MAX) {
				printf("Extreme Wealth\n");
				return 0;
			}
		}
	}
	if (result > MAX) {
		printf("Extreme Wealth\n");
	}
	else {
		printf("%.50Lf\n", result);
	}
}
