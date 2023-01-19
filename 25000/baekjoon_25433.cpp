#define private public
#include <bitset>
#undef private
#include <bits/stdc++.h>
#include <x86intrin.h>
using namespace std;
string s, t;
char x, y;
template<size_t _Nw> void _M_do_sub(_Base_bitset<_Nw>& A, const _Base_bitset<_Nw>& B) {
    for (size_t i = 0, c = 0; i < _Nw; i++) {
        c = _subborrow_u64(c, A._M_w[i], B._M_w[i], (unsigned long long*) & A._M_w[i]);
    }
}
template<> void _M_do_sub(_Base_bitset<1>& A, const _Base_bitset<1>& B) {
    A._M_w -= B._M_w;
}
template<size_t _Nb> bitset<_Nb>& operator-=(bitset<_Nb>& A, const bitset<_Nb>& B) {
    return _M_do_sub(A, B), A;
}

template<size_t _Nb> inline bitset<_Nb> operator-(const bitset<_Nb>& A, const bitset<_Nb>& B) {
    bitset<_Nb> C(A);
    return C -= B;
}

size_t Bitset(string s1, string s2) {
    bitset<50000> D, Match[26];
    for (size_t i = 0; i < s2.size(); i++) {
        Match[s2[i] - 'a'][i] = 1;
    }
    for (size_t i = 0; i < s1.size(); i++) {
        auto x = Match[s1[i] - 'a'] | D, y = D << 1;
        y[0] = 1;
        D = x ^ (x & (x - y));
    }
    return D.count();
}
bool isPrime(int n) {
    if (n == 1 || n == 0) {
        return false;
    }
    for (int i = 2; i <= static_cast<int>(sqrt(n)); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
int main() {
    cin >> s >> t >> x >> y;
    s.erase(remove(s.begin(), s.end(), y), s.end());
    t.erase(remove(t.begin(), t.end(), y), t.end());
    size_t pos_s = s.find(x), pos_t = t.find(x);
    for (int i = static_cast<int>(Bitset(s.substr(0, pos_s), t.substr(0, pos_t))) + static_cast<int>(Bitset(s.substr(pos_s + 1), t.substr(pos_t + 1))) + 1; i >= 0; i--) {
        if (isPrime(i)) {
            cout << i << '\n';
            return 0;
        }
    }
    cout << -1 << '\n';
}
