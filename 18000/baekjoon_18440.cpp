/*
#define private public
#include <bitset>
#undef private
#include <bits/stdc++.h>
#include <x86intrin.h>
using namespace std;
template<size_t _Nw> void _M_do_sub(_Base_bitset<_Nw>& A, const _Base_bitset<_Nw>& B) {
	for (int i = 0, c = 0; i < _Nw; i++) c = _subborrow_u64(c, A._M_w[i], B._M_w[i], (unsigned long long*) & A._M_w[i]);
}
template<> void _M_do_sub(_Base_bitset<1>& A, const _Base_bitset<1>& B) { A._M_w -= B._M_w; }
template<size_t _Nb> bitset<_Nb>& operator-=(bitset<_Nb>& A, const bitset<_Nb>& B) { return _M_do_sub(A, B), A; }
template<size_t _Nb> inline bitset<_Nb> operator-(const bitset<_Nb>& A, const bitset<_Nb>& B) { bitset<_Nb> C(A); return C -= B; }
string s, t, lcs;
template<size_t sz>
vector<int> Bitset(int s1, int s2, int t1, int t2, bool Reversed = false) {
	bitset<sz> D, x, S[26];
	if (!Reversed) {
		for (int i = t1; i <= t2; i++) {
            S[t[i] - 'A'][i - t1] = 1;
        }
		for (int i = s1; i <= s2; i++) {
			x = S[s[i] - 'A'] | D;
			D <<= 1;
            D[0] = 1;
			D = x & (x ^ (x - D));
		}
		vector<int> ret(t2 - t1 + 3);
		for (int i = t1; i <= t2; i++) {
            ret[i - t1 + 1] = ret[i - t1] + D[i - t1];
        }
		return ret;
	}
	else {
		for (int i = t2; i >= t1; i--)
        S[t[i] - 'A'][t2 - i] = 1;
		for (int i = s2; i >= s1; i--) {
			x = S[s[i] - 'A'] | D;
			D <<= 1, D[0] = 1;
			D = x & (x ^ (x - D));
		}
		vector<int> ret(t2 - t1 + 3);
		for (int i = t2; i >= t1; i--) ret[i - t1 + 1] = ret[i - t1 + 2] + D[t2 - i];
		return ret;
	}
}
vector<int> LCS(int s1, int s2, int t1, int t2, bool Reversed = false) {
	int SIZE = t2 - t1 + 1;
	if (SIZE <= 64)
        return Bitset<64>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 128)
        return Bitset<128>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 256)
        return Bitset<256>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 512)
        return Bitset<512>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 1024)
        return Bitset<1024>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 2048)
        return Bitset<2048>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 4096)
        return Bitset<4096>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 8192)
        return Bitset<8192>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 16384)
        return Bitset<16384>(s1, s2, t1, t2, Reversed);
	if (SIZE <= 32767)
        return Bitset<32767>(s1, s2, t1, t2, Reversed);
	return Bitset<65536>(s1, s2, t1, t2, Reversed);
}
void Hirschburg(int s1, int s2, int t1, int t2) {
	int S = (s1 + s2) / 2, T = 0, MAX = -1;
	if (s1 > s2) return;
	if (s1 == s2) {
		for (int i = t1; i <= t2; i++) {
            if (t[i] == s[s1]) {
                lcs.push_back(t[i]);
                break;
            }
        }
		return;
	}
	auto LCS1 = LCS(s1, S, t1, t2, false);
	auto LCS2 = LCS(S + 1, s2, t1, t2, true);
	for (int i = t1; i <= t2 + 1; i++) {
		if (MAX < LCS1[i - t1] + LCS2[i - t1 + 1]) {
			MAX = LCS1[i - t1] + LCS2[i - t1 + 1];
            T = i;
        }
	}
	Hirschburg(s1, S, t1, T - 1);
	Hirschburg(S + 1, s2, T, t2);
}
int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin >> s >> t;
	Hirschburg(0, s.size() - 1, 0, t.size() - 1);
	cout << lcs.size() << '\n' << lcs << '\n';
}
*/
