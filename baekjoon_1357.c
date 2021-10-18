#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
int rev(int n);
int main() {
	int x, y;
	scanf("%d %d", &x, &y);
	printf("%d", rev(rev(x) + rev(y)));
	return 0;
}
int rev(int n) {
	int temp = 0;
	while (n > 0) {
		temp *= 10;
		temp += n % 10;
		n /= 10;
	}
	return temp;
}
