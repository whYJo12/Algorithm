from collections import deque

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

r, c = map(int, input().split())
visited = [[False]*5 for _ in range(5)]

def bfs(x,y):
    dq = deque([(x, y, 0)])
    visited[x][y] = True

    while dq:
        x, y, cnt = dq.popleft()

        if graph[x][y] == 1:  # 1에 도착하면
            return cnt

        for i in range(4):   # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if 0 <= nx < 5 and 0 <= ny < 5:
                # 방문하지 않았고 -1(이동불가)이 아니라면
                if not visited[nx][ny] and graph[nx][ny] != -1:
                    visited[nx][ny] = True
                    dq.append([nx, ny, cnt+1])

    return -1    # 현재 칸 까지 이동한 횟수 리턴

print(bfs(r,c))