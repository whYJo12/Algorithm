from collections import deque

N, M, V = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)] #초기값을 False로 만든 그래프를 선언

for _ in range(M):  #간선만큼 반복
    a, b = map(int, input().split())    #연결된 정점을 입력받아 해당 위치를 True로 변경
    graph[a][b] = True
    graph[b][a] = True

visitedDFS = [False] * (N+1)    #DFS의 방문기록
visitedBFS = [False] * (N+1)    #BFS의 방문기록

def dfs(V):
    visitedDFS[V] = True    # 해당 V값 방문처리
    print(V, end=" ")   # 방문 후에 정점을 출력한다
    for i in range(1, N + 1):   # 1부터 N까지 돈다
        if not visitedDFS[i] and graph[V][i]:   # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다 (더 깊이 탐색) 재귀

def bfs(V):
    q = deque([V])  # 방문할 곳을 순서대로 넣을 큐 선언
    visitedBFS[V] = True    # 해당 V값 방문처리
    while q:    # q가 빌때까지 돈다
        V = q.popleft() # 큐에 있는 첫번째 값을 꺼낸다
        print(V, end=" ")    # 해당 값 출력
        for i in range(1, N + 1):   # 1부터 N까지 돈다
            if not visitedBFS[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i) # 그 i값을 추가
                visitedBFS[i] = True    #i값을 방문처리

dfs(V)
print()
bfs(V)
