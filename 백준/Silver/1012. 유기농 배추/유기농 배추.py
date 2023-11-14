T = int(input())

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    queue = [(x, y)]
    graph[x][y] = 0 #방문처리

    while queue:
        x, y = queue.pop(0)

        for i in range(4):   # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

# 행렬만들기
for i in range(T):
    M, N, K = map(int, input().split()) #M:가로길이 N:세로길이 K:배추위치개수
    graph = [[0] * (N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)