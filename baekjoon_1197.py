from sys import stdin
answer = 0 # 최종 가중치를 저장할 변수 저장
v, e = map(int, stdin.readline().split()) # 정점의 개수, 간선의 개수 입력
vroot = [i for i in range(v + 1)] # vroot라는 리스트의 크기는 간선 개수 
elist = sorted([list(map(int, stdin.readline().split())) for i in range(e)], key = lambda x: x[2])
# elist 에 간선의 가중치를 기준으로 오름차순으로 [정점1, 정점2, 가중치] 를 정렬
def find(x): # find 함수 선언
    if x != vroot[x]: # 만약 x가 vroot
        vroot[x] = find(vroot[x])
    return vroot[x]
for s, e, w in elist:
    sroot = find(s) # 간선이 잇는 두 정점의 root를 찾는다.
    eroot = find(e) # 간선이 잇는 두 정점의 root를 찾는다.
    if sroot != eroot: # 만약 sroot 와 eroot가 다르다면 큰 값을 작은 값으로 만든다.
        if sroot > eroot: 
            vroot[sroot] = eroot 
        else:
            vroot[eroot] = sroot
        answer += w # 최종 가중치에 현재 간선의 가중치를 더한다.
print(answer) # 최종 가중치 출력
