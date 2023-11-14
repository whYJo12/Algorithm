from collections import deque

# 이동할 여덟가지 방향 정의 (상하좌우대각선)
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

M, N = map(int, input().split()) #M:가로길이 N:세로길이
graph = []
cnt = 0

for _ in range(M):
    graph.append(list(map(int, input().split())))

def bfs(x,y):
    queue = deque()
    queue.append((a, b))
    graph[x][y] = 0 #방문처리

    while queue:
        x, y = queue.popleft()

        for i in range(8):   # 8가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

for a in range(M):
    for b in range(N):
        if graph[a][b] == 1:
            bfs(a, b)
            cnt += 1
print(cnt)
