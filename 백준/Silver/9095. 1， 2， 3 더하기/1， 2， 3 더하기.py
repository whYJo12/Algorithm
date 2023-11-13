def function():
    T = int(input())

    for i in range(T):
        X = int(input())
        dp = [0] * (X+1)
        if X == 1:  #dp[1] ~ dp[3]은 답이 정해져 있음
            print(1)
        elif X == 2:
            print(2)
        elif X == 3:
            print(4)
        else:
            dp[1] = 1
            dp[2] = 2
            dp[3] = 4
            for j in range(4, X + 1):
                dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
            print(dp[X])

if __name__ == "__main__":
    function()
