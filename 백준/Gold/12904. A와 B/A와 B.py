def function():
    S = input()
    T = input()
    flag = False

    while len(S) <= len(T):
        if S != T:
            if T.rfind('A') == len(T)-1:
                T = T[:-1]

            else:
                T = T[:-1]
                T = T[::-1]

        else:
            flag = True
            break

    if flag:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    function()