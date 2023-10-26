from collections import deque

N = int(input())  # 컴퓨터의 수 (노드)
M = int(input())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터의 쌍 (간선)
graph = [[False]*(N+1) for _ in range(N+1)] # 초기값을 False로 만든 그래프를 선언

for _ in range(M):  # 간선만큼 반복
    a, b = map(int, input().split())    # 연결된 정점을 입력받아 해당 위치를 True로 변경
    graph[a][b] = True
    graph[b][a] = True

visitedDFS = [False] * (N+1)    # DFS의 방문기록
worm = []   # 바이러스에 걸린 컴퓨터 리스트

def dfs(V):
    visitedDFS[V] = True    # 해당 V값 방문처리
    #print(V, end=" ")   # 방문 후에 정점을 출력한다
    for i in range(1, N + 1):   # 1부터 N까지 돈다
        if not visitedDFS[i] and graph[V][i]:   # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다 (더 깊이 탐색) 재귀
    worm.append(V)

dfs(1) # 1번 컴퓨터 부터 시작
print(len(worm)-1)  # 1번 컴퓨터를 통해 웜바이러스에 걸린 컴퓨터의 수 출력
