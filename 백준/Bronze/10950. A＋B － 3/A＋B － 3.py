import sys

def function():
    T = int(input())  # 테스트 케이스 수

    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())

        print(A+B)

if __name__ == "__main__":
    function()