#include <bits/stdc++.h>
using namespace std;
#define MAXN 50000
void Set(int N, uint64_t* dest, int k) {
    int n = k >> 6; int b = k & 63;
    dest[n] |= uint64_t(1) << (63 - b);
}
bool isset(int N, uint64_t* dest, int k) {
    int n = k >> 6; int b = k & 63;
    return (dest[n] & uint64_t(1) << (63 - b));
}
void clear(int N, uint64_t* dest) {
    N = (N + 63) >> 6;
    memset(dest, 0, N * sizeof(uint64_t));
}
void rshiftor(int N, int k, uint64_t* src, uint64_t* dest) {
    int rN = N;
    N = (N + 63) >> 6;
    int n = k >> 6; int b = k & 63;
    if (b) {
        dest[n] |= src[0] >> b;
        for (int i = 1; n + i < N; ++i)
            dest[n + i] |= (src[i - 1] << (64 - b)) | (src[i] >> b);
    }
    else {
        for (int i = 0; n + i < N; ++i)
            dest[n + i] |= src[i];
    }
    int rem = rN & 63;
    if (rem) {
        uint64_t mask = (uint64_t(1) << (64 - rem)) - 1;
        dest[N - 1] &= ~mask;
    }
}
void lshiftor(int N, int k, uint64_t* src, uint64_t* dest) {
    int rN = N;
    N = (N + 63) >> 6;
    int n = k >> 6; int b = k & 63;
    if (b) {
        for (int i = 0; n + i + 1 < N; ++i)
            dest[i] |= (src[n + i] << b) | (src[n + i + 1] >> (64 - b));
        dest[N - n - 1] |= src[N - 1] << b;
    }
    else {
        for (int i = 0; n + i < N; ++i)
            dest[i] |= src[n + i];
    }
    int rem = rN & 63;
    if (rem) {
        uint64_t mask = (uint64_t(1) << (64 - rem)) - 1;
        dest[N - 1] &= ~mask;
    }
}
void bitcopy(int N, uint64_t* src, uint64_t* dest) {
    N = (N + 63) >> 6;
    memcpy(dest, src, N * sizeof(uint64_t));
}
uint64_t dp[MAXN][(MAXN + 63) / 64];
vector<bool> ErdosGinzburgZiv(int, vector<int>);
vector<bool> ErdosGinzburgZivPrime(int p, vector<int> arr) {
    if (p == 1) return { true };
    vector<bool> ret(p * 2 - 1, false);
    for (int i = 0; i < p * 2 - 1; i++) {
        arr[i] %= p;
    }
    vector<int> idx(2 * p - 1); iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), [&](int a, int b) {
        return arr[a] < arr[b]; }
    );
    for (int i = 0; i < p; ++i) {
        if (arr[idx[i]] == arr[idx[i + p - 1]]) {
            for (int j = i; j < i + p; ++j) ret[idx[j]] = true;
            return ret;
        }
    }
    int imod = 0;
    for (int i = 0; i < p; i++) {
        imod += arr[idx[i]];
        if (imod >= p) {
            imod -= p;
        }
        ret[idx[i]] = true;
    }
    if (imod == 0) {
        return ret;
    }
    clear(p, dp[0]); Set(p, dp[0], imod);
    int i;
    for (i = 1; i < p; ++i) {
        int d = arr[idx[i + p - 1]] - arr[idx[i]];
        bitcopy(p, dp[i - 1], dp[i]);
        rshiftor(p, d, dp[i - 1], dp[i]);
        lshiftor(p, p - d, dp[i - 1], dp[i]);
        if (isset(p, dp[i], 0)) break;
    }
    int cur = 0;
    for (int j = i; j >= 1; --j) {
        int d = arr[idx[j + p - 1]] - arr[idx[j]];
        int ncur = cur - d; if (ncur < 0) ncur += p;
        if (isset(p, dp[j - 1], ncur)) {
            ret[idx[j]] = false;
            ret[idx[j + p - 1]] = true;
            cur = ncur;
        }
    }
    return ret;
}
vector<bool> ErdosGinzburgZivComposite(int a, int b, vector<int> arr) {
    vector<vector<int> > index;
    vector<int> index_vector;
    int tp = 0;
    for (int _ = 0; _ < a - 1; _++) {
        index_vector.push_back(tp++);
    }
    for (int i = 0; i < 2 * b - 1; ++i) {
        for (int j = 0; j < a; ++j) index_vector.push_back(tp++);
        vector<int> recur_vector(a * 2 - 1);
        for (int i = 0; i < a * 2 - 1; ++i) {
            recur_vector[i] = arr[index_vector[i]];
        }
        vector<bool> recur_answer = ErdosGinzburgZiv(a, recur_vector);
        vector<int> push_index, remain_index;
        for (int i = 0; i < a * 2 - 1; ++i) {
            if (recur_answer[i]) {
                push_index.push_back(index_vector[i]);
            }
            else {
                remain_index.push_back(index_vector[i]);
            }
        }
        index_vector = remain_index;
        index.push_back(push_index);
    }
    vector<int> sum_vector(b * 2 - 1);
    for (int i = 0; i < b * 2 - 1; ++i) {
        long long temp = 0;
        for (int j = 0; j < a; j++) {
            temp += arr[index[i][j]];
        }
        sum_vector[i] = temp / a % b;
    }
    vector<bool> rec = ErdosGinzburgZiv(b, sum_vector);
    vector<bool> ret(a * b * 2 - 1, false);
    for (int i = 0; i < b * 2 - 1; i++)
        if (rec[i])
            for (int j : index[i])
                ret[j] = true;
    return ret;
}
vector<bool> ErdosGinzburgZiv(int N, vector<int> arr) {
    for (int i = 2; i < N; i++) {
        if (!(N % i)) {
            return ErdosGinzburgZivComposite(i, N / i, arr);
        }
    }
    return ErdosGinzburgZivPrime(N, arr);
}
int main() {
    int N, t;
    cin >> N;
    vector<int> V;
    for (int i = 0; i < N * 2 - 1; i++) {
        cin >> t;
        V.push_back(t);
    }
    vector<bool> result = ErdosGinzburgZiv(N, V);
    for (int i = 0; i < N * 2 - 1; i++) {
        if (result[i]) {
            cout << V[i] << " ";
        }
    }
    cout << '\n';
    return 0;
}
