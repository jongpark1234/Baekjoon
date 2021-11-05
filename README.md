# Baekjoon Online Judge
## My Profile
[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=jongpark1234)](https://solved.ac/jongpark1234)
[![hyp3rflow's solved.ac stats](https://github-readme-solvedac.hyp3rflow.vercel.app/api/?handle=jongpark1234)](https://www.acmicpc.net/user/jongpark1234)

## Algorithms
### 수학 (Mathematics)
**수학적인 방법으로 접근하여 문제를 해결해야하는 문제로 이루어져 있습니다.**
+ **대표 문제 : [2609 - 최대공약수와 최소공배수](https://www.acmicpc.net/problem/2609)**
### 구현 (Implementation)
**구현은 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정입니다.**  
**구현 유형에는 완전 탐색, 시뮬레이션이 있으며,**  
**완전 탐색은 모든 경우의 수를 주저 없이 다 계산하는 해결 방법이고,**  
**시뮬레이션은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해서 해결해야 합니다.**
+ **대표 문제 : [14499 - 주사위 굴리기](https://www.acmicpc.net/problem/14499)**
### 다이나믹 프로그래밍 (Dynamic Programming)
**동적 계획법은  "어떤 문제를 풀기 위해 그 문제를 더 작은 문제의 연장선으로 생각하고,**  
**과거에 구한 해를 활용하는" 방식의 알고리즘을 총칭합니다.**

![DNPG](https://blog.kakaocdn.net/dn/cmWrJH/btqG3lKtdFX/PLuok65B4W3v86mLXQKyo0/img.png "Dynamic Programming")
+ **대표 문제 : [1509 - 팰린드롬 분할](https://www.acmicpc.net/problem/1509)**  
　　　　　**[16500 - 문자열 판별](https://www.acmicpc.net/problem/16500)**  
　　　　　**[20500 - Ezreal 여눈부터 가네 ㅈㅈ](https://www.acmicpc.net/problem/20500)**
### 그래프 이론 (Graph Theory)
**그래프 이론은 수학에서 객체 간에 짝을 이루는 관계를**  
**모델링하기 위해 사용되는 수학 구조인 그래프에 대한 연구입니다.**

![GT](https://miro.medium.com/max/1000/1*GyYtQ1e26aSO5lsk9G_ZjA.jpeg "Graph Theory")
+ **대표 문제 : [2667 - 단지번호붙이기](https://www.acmicpc.net/problem/2667)**
### 자료 구조 (Data Structure)
**자료 구조는 효율적인 접근 및 수정을 가능케 하는 자료의 조직, 관리, 저장을 의미합니다.**  
**효과적으로 설계된 자료구조는 실행시간 혹은 메모리 용량과 같은 자원을 최소한으로 사용하면서 연산을 수행하도록 해 줍니다.**

![DS](https://1.bp.blogspot.com/-xIvY2zPVe0E/XDsYHAO93BI/AAAAAAAAKx8/pRmZ4xKdNkwzbdJDlzsI3UX-j57KiKLKwCLcBGAs/s1600/111.png "Data Structure")
+ **대표 문제 : [3190 - 뱀](https://www.acmicpc.net/problem/3190)**  
　　　　　**[4949 - 균형잡힌 세상](https://www.acmicpc.net/problem/4949)**
### 문자열 (String)
**문자열 알고리즘은 대표적으로 두 가지로 나눌 수 있습니다.**
#### 문자열 검색 (String Search)
**문자열 검색은 어떤 문자열 S에서 어떤 패턴 P를 찾아내는 알고리즘입니다. 문자열 집합에서 어느 한 개의 문자열을 탐색하는 알고리즘은 'Trie' 또는 '이진 탐색'을 참고하시기 바랍니다.**  
**문자열 검색은 크게 네 가지로 분류할 수 있습니다.**
##### Naïve String Search
**우직한 문자열 검색법이라는 이름 그대로, 첫 번째부터 n번째 글자까지, 2번째부터 m + 1번째 글자까지,   이런식으로 문자열을 일일이 찾아가며 탐색합니다.**

**이 경우 길이가 각각 n, m인 문자열과 패턴에 대해 `Θ((n − m) m)`의 탐색횟수를 거칩니다.**

**작동 시간은 오래 걸리나 구현이 편하여, 작은 입력에 대한 알고리즘에 쓰입니다.**
###### 예시 코드
~~~cpp
#include <iostream>
#include <string>

using namespace std;

void find_pattern(const string &, const string &);

int main(const int argc, const char **argv)
{
    const string haystack = "hello hello hello hellchosun";
    const string needle = "hell";

    find_pattern(haystack, needle);

    return 0;
}

void find_pattern(const string &haystack, const string &needle)
{
    const auto haystack_size = haystack.size();
    const auto needle_size = needle.size();
    size_t i;
    size_t j;
    bool unmatched_flag = true;

    cout << "Begin to find pattern \"" << needle << "\" at target string \"" << haystack << "\"" << endl;

    for (int i = 0; i < haystack_size - needle_size; ++i)
    {
        for (int j = 0; j < needle_size; ++j)
        {
            if (haystack[i + j] == needle[j])
            {
                continue;
            }

            break;
        }

        if (j == needle_size)
        {
            cout << "Pattern \"" << needle << "\" matched at " << i + 1 << " ~ " << i + 1 + needle_size << endl;

            unmatched_flag = false;
        }
    }

    if (unmatched_flag)
    {
        cout << "Pattern unmatched" << endl;
    }
}
~~~
##### Finite-state automaton based search
**오토마타라고 부르기도 하는 일고리즘입니다. 선형 시간의 효율성을 자랑하지만 후술할 KMP 알고리즘이 해당 알고리즘보다 빠르고 더 이해하기 쉽습니다.**

**이 알고리즘은 상태전이함수를 만들어야 하는데, 그 탐색횟수까지 고려해야 합니다. 따라서 전체 탐색 횟수는 `Θ(n + m ∣Σ∣)`이며, 이 때 ∣Σ∣는 문자열에 속해 있는 문자 종류의 개수입니다.**

**상태를 나타내는 p, 현재 문자열의 위치에 있는 문자의 종류를 나타내는 q가 있다면 상태전이 함수 `p = δ[p][q]` 를 n번 반복해주다가 최종 상태에 돌입하면 매칭된 위치를 출력해줍니다.**

##### Knuth-Morris-Pratt Algorithm
**보통 발견자들의 앞글자를 따 KMP 알고리즘이라 하기도 합니다.**

**앞에서 설명한 오토마타와 비슷한 형식을 따르나 상태전이함수가 훨씬 간결하며, 준비 과정도 선형 시간인 점을 생각하면 문자의 종류가 다양한 상황에서는 당연히 KMP를 선택해야 메모리, 시간 모두 이득을 볼 수 있습니다.**

**KMP의 사용 방법은 다음과 같습니다.**

+ "abcdabckl" 이라는 문자열이 있다고 합니다. 이 때 i = -1, j = 0이며, 시작 위치의 상태함수에 들어갈 값은 -1입니다.
1. i와 j를 한 칸씩 전진시킨 뒤 비교합니다.
2. i와 j가 매치되면, 또는 i가 -1일 때 한 칸씩 전진한 뒤, j 위치에 i 를 저장합니다.
3. 만약 i 와 j 가 매치되지 않는다면 i는 상태전이함수에 있는 값으로 전환하고 2번으로 돌아갑니다.
4. 이 과정을 j 가 n 보다 커질 때까지 반복합니다.
5. 이 과정을 거친 상태전이함수는 0 0 0 0 1 2 3 0 0 이 됩니다.

**이 때의 계산횟수는 $Θ(n + m)$ 입니다.**
###### 예시 코드
~~~cpp
//상태전이함수 생성
void kmp(char *pat) {
    int n = strlen(pat);
    int i = -1, j = 0;
    pi[j] = i;
    while(j < n) {
        if(i == -1 || pat[i] == pat[j])
            pi[++j] = ++i;
        else 
            i = pi[i];
    }
}

//문자열 비교
void find_pattern(char *arr, char *pat) {
    int n = strlen(arr);
    int m = strlen(pat);
    int i = j = 0;
    while(i < n) {
        if(j == -1 || arr[i] == pat[j]) 
            i++, j++;
        else
            j = pi[j];
        
        if(j == m) {
            printf("The matching %d\n",i-m+1);
            j = pi[j];
        }
    }
}
~~~
##### Rabin-Karp String Search
**라빈 카프 알고리즘은 해시를 이용하여 해시끼리 비교하는 알고리즘입니다.**
+ 우선 찾으려는 패턴의 해시값을 구합니다.
+ 그리고 문자열의 앞에서부터 뒤까지 해시 값을 이동시킵니다.
+ 이 때 mod 연산을 사용하므로 앞에서 $26^{m-1} \times p \enspace mod \enspace q$를 뺀 뒤, 그 값에다가 26을 곱하고 이 때 다시 mod 연산을 취한 후 뒤에 자리를 더합니다.

**러빈 카프 알고리즘은 문자열이 매우 커질 경우 해시 충돌이 일어날 가능성이 커지므로 상당히 불안정하고 비효율적입니다. 하지만 현실세계에서의 문자열은 1억자리 이상 넘어가는 경우는 드뭅니다. 또한 KMP 보다 빠른 경우가 존재합니다. 해시를 사용하므로 시간복잡도는 평균적으로 `O(n + m)` 입니다.**
###### 예시 코드
~~~cpp
#define mod 1000000009
long long make_hash_p(char str[], int _size) {
	int i;
	long long hash_p = 0;
	for (i = 0; i < _size; i++) {
		hash_p *= 26;
		hash_p += str[i];
		hash_p %= mod;
	}
	return hash_p;
}
void match_s(char str[], int _size, int _size_p, long long hash_p) {
	int i;
	long long hash_s = 0;
	long long last = 1;
	for (i = 0; i < _size_p; i++) {
		hash_s *= 26;
		hash_s += str[i];
		hash_s %= mod;

		if (i == _size_p - 1) continue;
		last *= 26;
		last %= mod;
	}
	for (i = _size_p; i <= _size; i++) {
		if (i >= _size_p) {
			if (hash_s == hash_p) printf("match %d\n", i - _size_p + 1);
			if (i == _size) break;

			hash_s -= last * str[i - _size_p];
			hash_s *= 26;
			hash_s += str[i];
			hash_s %= mod;
			if (hash_s < 0) hash_s += mod; //빼는 과정에서 해시값이 음수가 되는 경우를 방지
		}
	}
}
~~~
#### 최장 공통 부분 문자열 (Longest Common Substring)
**LCS는 두 문자열이 주어졌을 때 최장 공통 부분 문자열을 찾는 알고리즘입니다.**

**생명과학 분야가 발전함에 따라 어떤 두 개의 염기 서열을 비교해야 하는 상황이 많이 나타났기 때문에 각종 알고리즘이 나온 분야이기도 합니다.**

##### Dynamic Programming
**다이나믹 프로그래밍으로 푸는 방법이 제일 잘 알려진 방법입니다.**

**두 문자열을 이용해서 일정한 규칙의 테이블을 만든 후,  
그 테이블을 살펴보면서 최장 공통 부분 문자열을 찾아낼 수 있습니다.**

**이 경우 테이블에 따라 계산하므로 시간 복잡도는 `O(n^2)` 입니다.**


**다이나믹 프로그래밍은 아래와 같은 가정을 거칩니다.**

1. 다음 식에 의해서 표를 생성합니다.
    + 0 ≤ i ≤ len(A)$ 이고 $0 ≤ j ≤ len(B) 일 때,
        + A[i] == B[j] 일 경우 LCSTable(i, j) = LCSTable(i - 1, j - 1) + 1
        + 아닐 경우 LCSTable(i, j) == 0
2. 표에서 가장 큰 숫자를 확인합니다.
    + A = BCBBBC, B = CBBBCC 인 경우

X　X　B　C　B　B　B　C

X　0　0　0　0　0　0　0

C　0　0　<span style="color:red">1</span>　0　0　0　<span style="color:red">1</span>

B　0　<span style="color:red">1</span>　0　<span style="color:red">2</span>　<span style="color:red">1</span>　<span style="color:red">1</span>　0

B　0　<span style="color:red">1</span>　0　<span style="color:red">1</span>　<span style="color:red">3</span>　<span style="color:red">2</span>　0

B　0　<span style="color:red">1</span>　0　<span style="color:red">1</span>　<span style="color:red">2</span>　<span style="color:red">4</span>　0

C　0　0　<span style="color:red">2</span>　0　0　0　<span style="color:red">**5**</span>

C　0　0　0　0　0　0　<span style="color:red">1</span>


3. 이 숫자들은 **공통 부분 문자열**의 길이를 나타내는 것으로, 대각선으로 왼쪽 위로 올라가면서 해당 문자를 확인해보게 되면 실제 최장 공통 부분 문자열(LCS)을 찾을 수 있습니다.  
위의 표에서 가장 큰 것은 **5**이므로, 대각선으로 올라가면서 문자를 확인해보면 "CBBBC"가 최장 공통 문자열임을 확인할 수 있습니다.
###### 예시 코드
~~~cpp
void find() {
    int i, j;
    int max1 = 0, tmpi = 0;
    for(i = 1; i <= n; i++) {
        for(j = 1; j <= m; j++) {
            if(s[i - 1] == p[j - 1]) dt[i][j] = dt[i - 1][j - 1] + 1;
            if(dt[i][j] > max1) {
                max1 = dt[i][j];
                tmpi = i;
            }
        }
    }
    printf("%d\n", max1);
    while(max1--) {
        ans[max1] = s[tmpi-1];
        tmpi--;
    }
    printf("%s", ans);
}
~~~
##### Suffix Array + LCP Array
**위의 다이나믹 프로그래밍의 시간 복잡도 `O(n^2)`는 실제 자연에서 볼 수 있는 염기 서열의 길이를 생각해보면 매우 오래 걸리며 메모리 낭비 역시 심합니다.**  
**수 많은 컴퓨터 과학자들과 수학자들이 이 문제에 대해 매달렸으며, Suffix Array는 이에 대한 해결법 중 하나입니다.**  

**비교하고자 하는 두 문자열을 합한 뒤, 그 문자열의 Suffix Array를 구했다면 LCP Array를 `O(n)` 만에 구할 수 있습니다.**  
**이 때의 LCP Array를 이용하여 LCS를 찾아낼 수 있습니다.**

**이 때의 탐색과 LCP Array를 만드는 데 걸리는 시간 복잡도는 `O(n)`이므로 Suffix Array를 구하는 시간 복잡도에 따라서 성능이 좌우됩니다.**
###### 예시 코드
~~~cpp
//Suffix Array 및 LCP Array 생성
bool cmp(int a, int b) {
    if (o[a] != o[b]) return o[a] < o[b];
    int x = a + gap;
    int y = b + gap;
    return ((x < n && y < n) ? o[x] < o[y] : x > y);
}
void makeSA() {
    int i;
    for (i = 0; i < n; i++) o[i] = s[i] - 'a', sa[i] = i;
    for (gap = 1;; gap < 1) {
        sort(sa, sa + n, cmp);
        tmp[0] = 0;
        for (i = 0; i < n - 1; i++) tmp[i + 1] = tmp[i] + cmp(sa[i], sa[i + 1]);
        if (tmp[n - 1] == n - 1) break;
        for (i = 0; i < n; i++) o[sa[i]] = tmp[i];
    }
}
void makeLCP() {
    int i, j;
    int k = 0;
    for (i = 0; i < n; i++) Rank[sa[i]] = i;
    for (i = 0; i < n; lcp[Rank[i++]] = k) {
        for ((k ? k-- : 0), j = (Rank[i] ? sa[Rank[i] - 1] : n); i + k < n && j + k < n && s[i + k] == s[j + k]; k++);
    }
}

int find() {
    int i;
    int max1 = 0, d;
    int h, t;
    bool sw = false;
    for (i = 0; i < n; i++) {
        if (sa[i] >= n - m) {
            t = 0x7fffffff;
            sw = true;
        } else if (sw) {
            h = n - sa[i] < lcp[i] ? n - sa[i] : lcp[i];
            t = t < h ? t : h;
            if (max1 < t) {
                max1 = t;
                d = sa[i];
            }
        }
    }
    sw = false;
    for (i = 0; i < n; i++) {
        if (sa[i] < n - m) {
            t = 0x7fffffff;
            sw = true;
        } else if (sw) {
            h = n - sa[i] < lcp[i] ? n - sa[i] : lcp[i];
            t = t < h ? t : h;
            if (max1 < t) {
                max1 = t;
                d = sa[i];
            }
        }
    }
    printf("%d\n", max1);
    for (i = d; i < d + max1; i++) printf("%c", s[i]);
    return 0;
}
~~~

+ **이 경우의 시간 복잡도는 `O(n log^2 n)` 입니다.**