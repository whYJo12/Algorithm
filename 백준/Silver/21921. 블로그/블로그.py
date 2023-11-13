import sys

def function():
    N, X = map(int, input().split())
    nList = list(map(int, sys.stdin.readline().strip().split()))
    sums = sum(nList[:X])
    sumsList = [sums]

    for i in range(N - X):
        sums = sums - nList[i] + nList[i+X]
        sumsList.append(sums)

    maxVisitor = max(sumsList)

    if maxVisitor == 0:
        print("SAD")
    else:
        print(max(sumsList))  # 최댓값 출력
        print(sumsList.count(max(sumsList)))

if __name__ == "__main__":
    function()