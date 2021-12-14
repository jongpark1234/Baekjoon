from sys import stdin, maxsize, setrecursionlimit
import heapq
setrecursionlimit(10**6) # 재귀함수의 최대 한도 설정
inf = maxsize # 무한 값 정의
v, e = map(int, stdin.readline().split()) # 정점의 개수 v, 간선의 개수 e
k = int(stdin.readline()) # 시작 정점 k
graph = [[] * (v + 1) for _ in range(v + 1)] # 각 0번째 인덱스는 쓰지않음
distance = [inf] * (v + 1) # 시작 정점으로부터 i번째까지 인덱스의 거리. 0번째 인덱스는 쓰이지않음
for _ in range(e): # 간선 입력받음
    U, V, W = map(int, stdin.readline().split()) # U 에서 V 로 가는 간선의 가중치는 W
    graph[U].append((V, W)) # 그래프 U번째 인덱스의 V번째는 W
def dijkstra(start): # 다익스트라 함수 ( 시작 지점 입력받음 )
    q = [] # 큐 선언
    heapq.heappush(q, (start, 0)) # q 에 시작지점, 가중치로 삽입
    distance[start] = 0 # 시작 노드와의 거리는 0
    while q: # 큐가 빌 때 까지 반복
        now, dist = heapq.heappop(q) # dist는 가중치, now는 현재 노드
        if distance[now] < dist: # 만약 이미 더 작은 가중치를 가지는 경로가 있을 경우
            continue # 컨티뉴
        for i in graph[now]: # 해당 그래프와 연결된 정점을 모두 탐색
            cost = dist + i[1] # 가중치는 현재 이 노드까지의 가중치와 신규 가중치를 더한 값
            if cost < distance[i[0]]: # 만약 산규 가중치가 현재 그 노드로 가는 가중치보다 작다면
                distance[i[0]] = cost # 값을 새로 갱신
                heapq.heappush(q, (i[0], cost)) # 해당 노드와 중첩된 가중치를 큐에 push
dijkstra(k) # 다익스트라 알고리즘 실행
for i in range(1, v + 1): # 1부터 시작
    if distance[i] == inf: # 만약 inf 값에 해당되면
        print('INF') # INF 출력
    else: # 아니면
        print(distance[i]) # 그대로 출력
