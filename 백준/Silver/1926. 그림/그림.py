from collections import deque

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())  # 가로, 세로
graph = []
paint = []   #그림
count = 0   #그림 수

for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(x, y):
    queue = deque()
    queue.append((a,b))
    graph[x][y] = 0  # 방문처리
    size = 1   #그림 사이즈
    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                size += 1
                queue.append((nx, ny))
                graph[nx][ny] = 0

    return size

for a in range(N):
    for b in range(M):
        if graph[a][b] == 1:
            paint.append(bfs(a, b))
            count += 1

if count == 0:
    print(count)
    print(0)
else:
    print(count)
    print(max(paint))