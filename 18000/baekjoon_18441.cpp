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
template<size_t sz>
string Bitset(const string& a, const string& b) {
    bitset<sz> x, S[26];
	vector<bitset<sz>> D(a.size() + 1);
	string ret;
    for (int i = 0; i < b.size(); i++) {
        S[b[i] - 'a'][i] = 1;
    }
    for (int i = 0; i < a.size(); i++) {
        x = S[a[i] - 'a'] | D[i];
		D[i + 1] = D[i] << 1, D[i + 1][0] = 1;
		D[i + 1] = x & (x ^ (x - D[i + 1]));
    }
	for (int x = a.size(), y = b.size() - 1; x > 0; x--) {
		while (y >= 0 && !D[x][y]) y--;
		if (y < 0) break;
		while (x > 0 && D[x - 1][y]) x--;
		ret.push_back(b[y--]);
	}
	reverse(ret.begin(), ret.end());
	return ret;
}
string LCS(const string& s, const string& t) {
	if (t.size() <= 64)
        return Bitset<64>(s, t);
	if (t.size() <= 128)
        return Bitset<128>(s, t);
	if (t.size() <= 192)
        return Bitset<192>(s, t);
	if (t.size() <= 256)
        return Bitset<256>(s, t);
	if (t.size() <= 320)
        return Bitset<320>(s, t);
	if (t.size() <= 384)
        return Bitset<384>(s, t);
	if (t.size() <= 448)
        return Bitset<448>(s, t);
	if (t.size() <= 512)
        return Bitset<512>(s, t);
	if (t.size() <= 576)
        return Bitset<576>(s, t);
	if (t.size() <= 640)
        return Bitset<640>(s, t);
	if (t.size() <= 704)
        return Bitset<704>(s, t);
	if (t.size() <= 768)
        return Bitset<768>(s, t);
	if (t.size() <= 832)
        return Bitset<832>(s, t);
	if (t.size() <= 896)
        return Bitset<896>(s, t);
	if (t.size() <= 960)
        return Bitset<960>(s, t);
	if (t.size() <= 1024)
        return Bitset<1024>(s, t);
	if (t.size() <= 1088)
        return Bitset<1088>(s, t);
	if (t.size() <= 1152)
        return Bitset<1152>(s, t);
	if (t.size() <= 1216)
        return Bitset<1216>(s, t);
	if (t.size() <= 1280)
        return Bitset<1280>(s, t);
	if (t.size() <= 1344)
        return Bitset<1344>(s, t);
	if (t.size() <= 1408)
        return Bitset<1408>(s, t);
	if (t.size() <= 1472)
        return Bitset<1472>(s, t);
	return Bitset<1536>(s, t);
}
int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);
	int T;
    cin >> T;
	for (int c = 1; c <= T; c++) {
		string s, MAX;
        cin >> s;
		for (int i = 1; i < s.size(); i++) {
			auto a = s.substr(0, i);
			auto b = s.substr(i, s.size());
			auto SquareLCS = a.size() > b.size() ? LCS(a, b) : LCS(b, a);
			if (MAX.size() < SquareLCS.size()) {
                MAX = SquareLCS;
            }
		}
		cout << "Case #" << c << ": " << 2 * MAX.size() << '\n';
		if (MAX.size()) cout << MAX << MAX << '\n';
	}
}
*/