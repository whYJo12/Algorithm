def function():
    N = int(input())
    h = list(map(int, input().split()))
    cnt = 0  # 2만큼 자라는 물뿌리개 횟수

    if sum(h) % 3 == 0:
        for i in h:
            cnt += i // 2
        if cnt >= (sum(h) / 3): # 나무가 자라나는데 걸리는 총 일수보다 2만큼 성장시키는 물뿌리개를 사용하는 횟수는 크거나 같아야한다.
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    function()