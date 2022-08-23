#include <bits/stdc++.h>
#include "registers.h"
using namespace std;
#define SIZE 2000
void solve(int t, int k, vector<bool> numlist, int l) {
    append_store(97, numlist);
    append_and(96, 97, 0);
    append_xor(95, 96, 0);
    append_right(95, 95, k * l);
    append_and(95, 95, 97);
    append_xor(94, 95, 97);
    append_add(93, 96, 94);
    append_right(93, 93, k);
    append_add(93, 93, 97);
    append_and(92, 96, 93);
    append_and(91, 95, 93);
    append_xor(95, 95, 91);
    append_xor(96, 96, 92);
    append_or(92, 92, 95);
    append_or(91, 91, 96);
    append_left(91, 91, k * l);
    append_or(t, 92, 91);
}
void construct_instructions(int s, int n, int k, int q) {
    vector<bool> v(SIZE);
    for (; (n & -n) != n; n++) {
        for (int i = 0; i < k; i++) {
            v[n * k + i] = true;
        }
    }
    append_store(1, v);
    append_or(0, 0, 1);
    for (int len = 1; len < n; len <<= 1) {
        for (int step = len; step > (s == 0 ? len - 1 : 0); step /= 2) {
            vector<bool> mask(SIZE);
            vector<bool> numvec1(SIZE);
            vector<bool> numvec2(SIZE);
            for (int i = 0; i + step < n; ++i) {
                if ((step == len && (i & step)) || (step != len && !(i & step)))
                    continue;
                if (i / (len << 1) != (i + step) / (len << 1))
                    continue;
                if ((i & 1) && step != 1) {
                    for (int j = 0; j < k; ++j) {
                        numvec2[i * k + j] = true;
                    }
                }
                else {
                    for (int j = 0; j < k; ++j) {
                        numvec1[i * k + j] = true;
                    }
                }
            }
            for (int i = 0; i < n; ++i) {
                if (numvec1[i * k] || numvec2[i * k])
                    continue;
                if (i >= step && (numvec1[(i - step) * k] || numvec2[(i - step) * k]))
                    continue;
                for (int j = 0; j < k; ++j) {
                    mask[i * k + j] = true;
                }
            }
            solve(1, k, numvec1, step);
            if (s != 0 && step != 1) {
                solve(2, k, numvec2, step);
            }
            if (step != len) {
                append_store(3, mask);
                append_and(3, 3, 0);
                append_or(1, 1, 3);
            }
            append_or(0, 1, s != 0 && step != 1 ? 2 : 1);
        }
    }
}
