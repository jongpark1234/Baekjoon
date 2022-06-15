/*
#include "network.h"
#include <vector>
using namespace std;
vector<int> dist[1001];
void findRoute(int N, int a, int b){
    int m1 = ping(a, b) + 1;
    for (int i = 1; i <= N; i++) {
        if (b == i) continue;
        int m2 = ping(b, i) + 1;
        if (m1 <= m2) continue;
        dist[m1 - m2].push_back(i);
    }
    int temp = a;
    for (int i = 1; i < m1; i++) {
        for (int j = 0; j < dist[i].size(); j++) {
            if (ping(temp, dist[i][j]) == 0) {
                travelTo(dist[i][j]);
                temp = dist[i][j];
                break;
            }
        }
    }
    travelTo(b);
}
*/
