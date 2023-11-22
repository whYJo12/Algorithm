# 투에모스 점화식을 이용
# t(0) = 0
# t(2n) = t(n)
# t(2n + 1) = 1 - t(n)

k = int(input())

def thue_morse(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x % 2 == 0:
        return thue_morse(x // 2)
    else:
        return 1 - thue_morse(x // 2)

# 인덱스 k-1을 포함한 투에모스 문자열의 길이 k에서 1을 빼준다.
print(thue_morse(k - 1))

