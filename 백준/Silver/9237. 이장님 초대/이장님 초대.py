def function():
    n = int(input())
    tree = list(map(int, input().split()))
    tree.sort(reverse=True)
    dayList = []

    for i in range(n):
        dayList.append(int(tree[i])+(i+1))

    dayList.sort(reverse=True)
    print(dayList[0]+1)

if __name__ == "__main__":
    function()