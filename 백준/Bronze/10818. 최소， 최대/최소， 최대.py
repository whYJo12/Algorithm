import sys

def function():
    N = int(input())
    num = list(map(int, input().split()))
    num.sort(reverse=True)

    print(str(num[N-1]) + " " + str(num[0]))

if __name__ == "__main__":
    function()