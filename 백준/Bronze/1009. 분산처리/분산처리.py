def function():
    T = int(input())
    ab = [list(map(int, input().split())) for _ in range(T)]

    for i in range(T):
        a = (int(ab[i][0]) % 10)
        b = int(ab[i][1])
        if a == 0:
            print(10)
        elif a == 1 or a == 5 or a == 6:
            print(a)
        elif a == 4 or a == 9:
            b = b % 2
            if b == 1:
                print(a)
            else:
                print((a * a) % 10)
        else:
            b = b % 4
            if b == 0:
                print((a**4) % 10 % 10 % 10)
            else:
                print((a**b) % 10 % 10 % 10)

if __name__ == "__main__":
    function()