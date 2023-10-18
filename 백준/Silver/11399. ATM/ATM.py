import sys

input = sys.stdin.readline
output = sys.stdout.write

def function():
    n = int(sys.stdin.readline())
    time_list = list(map(int, sys.stdin.readline().split())) # 리스트 형태로 입력
    total = 0

    time_list.sort() # 작은 순서대로 정렬
    for i in range(1, n+1):
        total += sum(time_list[0:i]) # 리스트의 0번째 수부터 x번째 수까지 더하기

    return total


if __name__ == "__main__":
    print(function())