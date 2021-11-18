from sys import *
setrecursionlimit(10**6) # 재귀 최대치 변경
n, m = map(int, stdin.readline().split()) # n , m 입력
graph = [[] for _ in range(n + 1)] # 그래프 선언
visited = [False for _ in range(n + 1)] # 방문 여부 리스트 선언
graph[0] = [0, 0] # 0번째는 무시
cnt = 0 # cnt 변수 선언
def dfs(s): # dfs 함수 선언
    visited[s] = True # 해당 번호 노드는 방문됨
    for i in graph[s]: # 해당 번호 노드의 자식 노드 확인
        if not visited[i]: # 만약 방문하지 않은 노드가 있다면
            dfs(i) # dfs 재귀
for i in range(m): # 간선을 m 번 입력받음
    s, e = map(int, stdin.readline().split()) # 시작부분 노드, 끝부분 노드 입력
    graph[s].append(e) # 두 노드에
    graph[e].append(s) # 서로 연결시킴
for i in range(1, n + 1): # 노드 개수만큼 반복
    if visited[i] == False: # 만약 방문하지 않은 노드면
        cnt += 1 # 연결 요소의 개수 + 1
        dfs(i) # dfs를 진행시켜 해당 노드랑 연결되어 있는 모든 노드 방문
print(cnt) # 연결 요소의 개수 출력
