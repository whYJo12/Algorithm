import sys

def function():
    N = int(input())
    nList = list(map(int, sys.stdin.readline().strip().split()))
    M = int(input())
    prefix_sum = [0] * (N + 1)

    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + nList[i]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().strip().split())
        partSum = prefix_sum[B] - prefix_sum[A - 1]
        print(partSum)

if __name__ == "__main__":
    function()