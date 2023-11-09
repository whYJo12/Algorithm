def function():
    while True:
        try:
            A, B = map(int, input().split())
            if A == 0 & B == 0:
                break
            else:
                print(A+B)
        except:
            break

if __name__ == "__main__":
    function()