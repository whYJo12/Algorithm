from collections import deque

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(x,y):
    dq = deque()
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()

        for i in range(4):   # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue

            # 미로이므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                dq.append([nx, ny])

    return graph[N-1][M-1]    # 현재 칸 까지 이동한 횟수 리턴

print(bfs(0,0))