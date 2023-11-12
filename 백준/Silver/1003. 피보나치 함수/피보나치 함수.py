def fibonacci(N):
    zeros = [1,0,1] #0이 출력되는 횟수 리스트
    ones = [0,1,1]  #1이 출력되는 횟수 리스트

    if N >= len(zeros):
        for i in range(len(zeros), N+1):
            zeros.append(zeros[i-1] + zeros[i-2])
            ones.append(ones[i-1] + ones[i-2])

    print(f"{zeros[N]} {ones[N]}")

T = int(input())

for _ in range(T):
    N = int(input())
    fibonacci(N)