import sys

def function():
    num = list([int(sys.stdin.readline()) for _ in range(9)])
    num2 = num.copy()
    num.sort(reverse=True)
    order = num2.index(num[0])

    print(num[0])
    print(order+1)

if __name__ == "__main__":
    function()