#include <bits/stdc++.h>
#define MAX 1000000
using namespace std;
string s, t;
void Hirschburg(int s1, int s2, int t1, int t2) {
    if (s1 > s2 || t1 > t2) {
        return;
    }
    if (s1 == s2) {
        for (int i = t1; i < t2; i++) {
            cout << "a " << t[i] << endl;
        }
        return;
    }
    if (t1 == t2) {
        for (int i = s1; i < s2; i++) {
            cout << "d " << s[i] << endl;
        }
        return;
    }
    pair<vector<int>, vector<int>> result;
    vector<int> temp;
    int m = s2 - s1 >> 1;
    for (int i = 0; i <= t2 - t1; i++) {
        result.first.push_back(i);
        result.second.push_back(t2 - t1 - i);
    }
    for (int i = 1; i <= m; i++) {
        temp = result.first;
        for (int j = 0; j <= t2 - t1; j++) {
            int minnum = MAX;
            bool flag = !(i && j && s[s1 + i - 1] == t[t1 + j - 1]);
            if (i > 0) {
                minnum = min(minnum, temp[j] + 1);
            }
            if (j > 0) {
                minnum = min(minnum, result.first[j - 1] + 1);
            }
            if (i > 0 && j > 0) {
                minnum = min(minnum, temp[j - 1] + flag);
            }
            result.first[j] = minnum;
        }
    }
    for (int i = s2 - s1 - 1; i > m; i--) {
        temp = result.second;
        for (int j = t2 - t1; j > -1; j--) {
            int minnum = MAX;
            bool flag = !(s[s1 + i] == t[t1 + j]);
            if (i < s2 - s1) {
                minnum = min(minnum, temp[j] + 1);
            }
            if (j < t2 - t1) {
                minnum = min(minnum, result.second[j + 1] + 1);
            }
            if (i < s2 - s1 && j < t2 - t1) {
                minnum = min(minnum, temp[j + 1] + flag);
            }
            result.second[j] = minnum;
        }
    }
    int minnum = MAX, l = -1, r = -1;
    for (int i = 0; i <= t2 - t1; i++) {
        if (minnum > result.first[i] + result.second[i] + 1) {
            minnum = result.first[i] + result.second[i] + 1;
            l = r = i;
        }
        if (i < t2 - t1) {
            bool flag = !(s[s1 + m] == t[t1 + i]);
            if (minnum > result.first[i] + result.second[i + 1] + flag) {
                minnum = result.first[i] + result.second[i + 1] + flag;
                l = i, r = i + 1;
            }
        }
    }
    Hirschburg(s1, s1 + m, t1, t1 + l);
    if (l != r) {
        cout << (s[s1 + m] != t[t1 + l] ? "m " : "c ") << t[t1 + l] << endl;
    }
    else {
        cout << "d " << s[s1 + m] << endl;
    }
    Hirschburg(s1 + m + 1, s2, t1 + r, t2);
}
int main() {
    cin >> s >> t;
    Hirschburg(0, s.size(), 0, t.size());
}
