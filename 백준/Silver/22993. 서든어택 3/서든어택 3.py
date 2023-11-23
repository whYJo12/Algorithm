import sys


def function():
    N = int(input())
    attackList = list(map(int, input().split()))
    flag = True
    gage = attackList[0]

    attackList.remove(gage)
    attackList.sort()

    for i in attackList:
        if gage > i:
            gage += i
        else:
            flag = False
            break
    print('Yes' if flag else 'No')

if __name__ == "__main__":
    function()
