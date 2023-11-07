import sys

def function():
    N = int(input())
    h = [int(sys.stdin.readline()) for _ in range(N)]
    h.sort(reverse=True)
    answer = -1

    for i in range(N-2):
        if h[i] < h[i+1] + h[i+2]: #어떤 삼각형이든 한 변의 길이가 나머지 두 변의 길이를 합한 것 보다 크거나 같을 수 없다
            answer = h[i] + h[i+1] + h[i+2]
            break
    print(answer)

if __name__ == "__main__":
    function()