# 이동할 네가지 방향 정의 (상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())  # 지도크기
graph = []
town = []   #단지내 집 수를 넣을 리스트
count = 0   #단지 수

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = [(x, y)]
    house = 1   #단지내 집의 수

    while queue:
        x, y = queue.pop(0)
        graph[x][y] = 0  # 방문처리

        for i in range(4):  # 4가지 방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                house += 1
                queue.append((nx, ny))
                graph[nx][ny] = 0

    return house

for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            th = bfs(a, b)  #각 단지내 집의 수
            town.append(th)
            count += 1

town.sort()
print(count)
for i in range(count):
    print(town[i])