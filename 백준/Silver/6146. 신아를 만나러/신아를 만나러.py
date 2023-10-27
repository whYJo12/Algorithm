from collections import deque

# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

X, Y, N = map(int, input().split())

graph = [[0]*1000 for _ in range(1000)]
for _ in range(N):
    A, B = map(int, input().split())
    graph[A][B] = -1

#print(*graph)
visited = [[False]*1000 for _ in range(1000)]

def bfs(x,y):
    dq = deque([(x, y, 0)])
    visited[x][y] = True

    while dq:
        x, y, cnt = dq.popleft()

        if x == X and y == Y:  # 1에 도착하면
            return cnt  # 현재 칸 까지 이동한 횟수 리턴

        for i in range(4):   # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가 (물웅덩이는 -500~500 사이에 있을 수 있음)
            if -500 <= nx < 500 and -500 <= ny < 500:
                # 방문하지 않았고 -1(이동불가)이 아니라면
                if not visited[nx][ny] and graph[nx][ny] != -1:
                    visited[nx][ny] = True
                    dq.append([nx, ny, cnt+1])

print(bfs(0,0))