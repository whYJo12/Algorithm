import sys

def function():
        N = int(input())
        num = list(sys.stdin.readline().rstrip())
        sum = 0

        for i in num:
            sum += int(i)

        print(sum)

if __name__ == "__main__":
    function()