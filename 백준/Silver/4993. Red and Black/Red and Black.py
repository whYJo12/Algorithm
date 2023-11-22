from collections import deque

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((a, b))
    graph[x][y] = 0  # 방문처리
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] == "#":
                continue

            # 빈공간이므로 이동
            if graph[nx][ny] == ".":
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count

while True:
    W, H = map(int, input().split())
    graph = []

    if W == 0 and H == 0:
        break

    for _ in range(H):
        graph.append(list(map(str, input())))

    for a in range(H):
        for b in range(W):
            if graph[a][b] == "@":
                count = bfs(a, b)

    print(count)
