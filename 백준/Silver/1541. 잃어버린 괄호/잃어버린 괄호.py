def function():
    formula = input()
    withoutMinus = formula.split('-')  # -를 기준으로 자름
    num = []

    for i in range(len(withoutMinus)):
        sum = 0
        withoutPlusStr = withoutMinus[i].split("+")
        for a in range(len(withoutPlusStr)):
            sum += int(withoutPlusStr[a])
        num.append(sum)

    n = num[0] # 제일 첫번째 숫자에서 나머지 값들을 뺀다

    for i in range(1, len(num)):
        n -= num[i]

    return n

if __name__ == "__main__":
    print(function())