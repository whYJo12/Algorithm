import sys

def function():
    A,B = [int(sys.stdin.readline()) for _ in range(2)]

    print(A+B)

if __name__ == "__main__":
    function()