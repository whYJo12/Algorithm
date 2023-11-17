from collections import deque
import sys
input = sys.stdin.readline

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[-1] * M for _ in range(N)] #방문기록

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 0  # 방문처리

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:

                # 갈 수 없는 땅이므로 진행 불가
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0 # 갈 수 없는 땅 체크

                # 갈 수 있는 땅이므로 이동
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]+1  # 방향 탐색 전에 위치값에 +1 하여 갈 수 있는 땅 체크
                    queue.append((nx, ny))

for a in range(N):
    for b in range(M):
        # 목표지점이고 visited[a][b]가 방문하지 않았을때
        if graph[a][b] == 2 and visited[a][b] == -1:
            bfs(a,b)

for a in range(N):
    for b in range(M):
        # graph[a][b]가 방문 못한 땅일때
        if graph[a][b] == 0:
            print(0, end=' ')
        # 방문했던 곳 일때
        else:
            print(visited[a][b], end=' ')
    print()