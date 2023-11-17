from collections import deque

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(str, input())))

def bfs(x, y):
    queue = deque()
    queue.append((a,b))
    graph[x][y] = 0  # 방문처리
    count = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] == "X":
                continue

            # 빈공간이므로 이동
            if graph[nx][ny] == "O":
                queue.append((nx, ny))
                graph[nx][ny] = 0

            if graph[nx][ny] == "P":
                count += 1
                queue.append((nx, ny))
                graph[nx][ny] = 0

    return count

for a in range(N):
    for b in range(M):
        if graph[a][b] == "I":
            count = bfs(a,b)

if count == 0:
    print("TT")
else:
    print(count)