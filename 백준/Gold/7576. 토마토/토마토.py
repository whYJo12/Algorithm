from collections import deque

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
res = 0
# 좌표를 넣기 때문에 []를 넣
queue = deque([])
graph = [list(map(int, input().split())) for _ in range(N)]

# queue에 처음에 받은 토마토의 위치 좌표를 append 시킨다
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가 & 익지 않은 토마토가 있어야함
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                # 익힌 후 1을 더해주면서 횟수를 세어주기
                # 제일 큰 값이 정답
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

bfs()

for a in graph:
    for b in a:
        # 다 돌았는데 토마토를 익히지 못했다면 -1 출력
        if b == 0:
            print(-1)
            exit(0)

    # 다 익혔다면 최댓값이 정답
    res = max(res, max(a))

# 첫 시작을 1로 표현했으니 1을 빼줌
print(res - 1)
