def function():

    X = int(input())
    dp = [0] * (X+1)

    for i in range(2, X + 1):
        dp[i] = dp[i - 1] + 1   #1을 빼는 연산을 먼저 1회 진행
        if i % 2 == 0:  #if를 사용해야 계산을 모두 거칠 수 있음
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[X])

if __name__ == "__main__":
    function()
