#define private public
#include <bitset>
#undef private
#include <iostream>
#include <string>
// #include <x86intrin.h>
std::string s, t;
template<std::size_t _Nw> void _M_do_sub(std::_Base_bitset<_Nw>& A, const std::_Base_bitset<_Nw>& B) {
    for (std::size_t i = 0, c = 0; i < _Nw; i++) {
        c = _subborrow_u64(c, A._M_w[i], B._M_w[i], (unsigned long long*) & A._M_w[i]);
    }
}
template<> void _M_do_sub(std::_Base_bitset<1>& A, const std::_Base_bitset<1>& B) {
    A._M_w -= B._M_w;
}
template<size_t _Nb> std::bitset<_Nb>& operator-=(std::bitset<_Nb>& A, const std::bitset<_Nb>& B) {
    return _M_do_sub(A, B), A;
}
template<size_t _Nb> inline std::bitset<_Nb> operator-(const std::bitset<_Nb>& A, const std::bitset<_Nb>& B) {
    std::bitset<_Nb> C(A);
    return C -= B;
}
std::size_t Bitset() {
    std::bitset<50000> D, Match[26];
    for (std::size_t i = 0; i < t.size(); i++) {
        Match[t[i] - 'A'][i] = 1;
    }
    for (std::size_t i = 0; i < s.size(); i++) {
        auto x = Match[s[i] - 'A'] | D;
        auto y = D << 1;
        y[0] = 1;
        D = x ^ (x & (x - y));
    }
    return D.count();
}
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
    std::cin >> s;
    std::cin >> t;
    std::cout << Bitset() << '\n';
}