import math

def function():
    T = int(input())  # 테스트 케이스 수

    for _ in range(T):  # 테스트 케이스 수 만큼 반복
        N, M = map(int, input().split())
        count = (math.factorial(M)) // (math.factorial(M-N)*math.factorial(N))

        print(count)

if __name__ == "__main__":
    function()