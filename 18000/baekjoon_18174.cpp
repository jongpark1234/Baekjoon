#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
#define INF 10000000000
int N, M, K, a, b, x = INF, y = INF, X = -INF, Y = -INF, n, m;
#define A (x - n)
#define B (N - X)
#define C (y - m)
#define D (M - Y)
#define XOR (A ^ B ^ C ^ D)
#define ZZ(S, N) (string(S) + " " + to_string(N))
string move() {
    int a;
    if ((XOR ^ A) < A) {
        return a = A - (XOR ^ A), n += a, ZZ("top", a);
    }
    if ((XOR ^ B) < B) {
        return a = B - (XOR ^ B), N -= a, ZZ("bottom", a);
    }
    if ((XOR ^ C) < C) {
        return a = C - (XOR ^ C), m += a, ZZ("left", a);
    }
    if ((XOR ^ D) < D) {
        return a = D - (XOR ^ D), M -= a, ZZ("right", a);
    }
}
int main(void) {
    scanf("%d %d %d", &N, &M, &K);
    for (int i = 0; i < K; i++) {
        scanf("%d %d", &a, &b), x = min(x, a), X = max(X, a), y = min(y, b), Y = max(Y, b);
    }
    --x, --y;
    if (XOR) {
        cout << move() << endl;
    }
    else {
        cout << "pass" << endl;
    }
    while (true) {
        string s;
        cin >> s;
        if (s == "yuck!") {
            return 0;
        }
        scanf("%d", &a);
        if (s == "top") {
            n += a;
        }
        else if (s == "bottom") {
            N -= a;
        }
        else if (s == "left") {
            m += a;
        }
        else if (s == "right") {
            M -= a;
        }
        cout << move() << endl;
    }
    return 0;
}
