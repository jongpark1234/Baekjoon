#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
mt19937_64 randrange(9875987250923849283);
bool visited[250001];
ull depth[250001], numlist1[250001], numlist2[250001], cl = 0;
vector<pair<ll, ll>> pairlist[250001];
map<ull, ll> cntmap;
void dfs(int i, int previous) {
    visited[i] = true;
    depth[i] = depth[previous] + 1;
    for (auto it : pairlist[i]) {
        int j = it.first, k = it.second;
        if (!visited[j]) {
            dfs(j, i);
            numlist2[k] = numlist1[j];
            numlist1[i] ^= numlist1[j];
        }
        else if (depth[j] < depth[i] - 1) {
            numlist2[k] = randrange();
            numlist1[i] ^= numlist2[k];
            numlist1[j] ^= numlist2[k];
            if ((depth[i] ^ depth[j] ^ 1) & 1) {
                cl ^= numlist2[k];
            }
        }
    }
}
ll count_ways(int N, vector<int> U, vector<int> V) {
    ll result = 0;
    int m, u, v;
    m = (int)U.size();
    for (int i = 0; i < m; i++) {
        u = U[i], v = V[i];
        pairlist[u].push_back({v, i});
        pairlist[v].push_back({u, i});
    }
    dfs(1, 0);
    if (cl == 0) {
        return 1;
    }
    for (int i = 0; i < m; i++) {
        if (numlist2[i] == cl)  {
            result++;
        }
    }
    if (result) {
        return result;
    }
    else {
        for (int i = 0; i < m; i++) {
            result += cntmap[cl ^ numlist2[i]];
            cntmap[numlist2[i]]++;
        }
        return result;
    }
}
