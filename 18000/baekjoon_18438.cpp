#include <iostream>
#include <string>
int LCS1[2][7001] = { 0, };
int LCS2[2][7001] = { 0, };
std::string s, t;
std::string Hirschburg(int s1, int s2, int t1, int t2)
{
    int S = (s1 + s2) / 2, T = 0, MAX = -1;
    std::string ret = "";
    if (s1 == s2) return "";
    if (s1 + 1 == s2) {
        for (int i = t1 + 1; i <= t2; i++) {
            if (s[s2] == t[i]) {
                ret += t[i];
                return ret;
            }
        }
        return "";
    }
    for (int i = t1; i <= t2; i++) {
        for (int j = 0; j < 2; j++) {
            LCS1[j][i] = 0;
            LCS2[j][i] = 0;
        }
    }
    for (int i = s1 + 1; i <= S; i++) {
        for (int j = t1 + 1; j <= t2; j++) {
            LCS1[i % 2][j] = s[i] == t[j] ? LCS1[(i + 1) % 2][j - 1] + 1 : std::max(LCS1[(i + 1) % 2][j], LCS1[i % 2][j - 1]);
        }
    }
    for (int i = s2 - 1; i >= S; i--) {
        for (int j = t2 - 1; j >= t1; j--) {
            LCS2[i % 2][j] = s[i + 1] == t[j + 1] ? LCS2[(i + 1) % 2][j + 1] + 1 : std::max(LCS2[(i + 1) % 2][j], LCS2[i % 2][j + 1]);
        }
    }
    for (int i = t1; i <= t2; ++i) {
        if (LCS1[S % 2][i] + LCS2[S % 2][i] > MAX) {
            MAX = LCS1[S % 2][i] + LCS2[S % 2][i];
            T = i;
        }
    }
    return Hirschburg(s1, S, t1, T) + Hirschburg(S, s2, T, t2);
}
int main()
{
    std::cin >> s;
    std::cin >> t;
    s.insert(s.begin(), 1234);
    t.insert(t.begin(), 1371);
    std::string lcs = Hirschburg(0, s.size() - 1, 0, t.size() - 1);
    std::cout << lcs.size() << '\n';
    std::cout << lcs << '\n';
}
