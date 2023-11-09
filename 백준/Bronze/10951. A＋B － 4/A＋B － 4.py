def function():
    while True:
        try:
            A, B = map(int, input().split())
            print(A+B)
        except:
            break

if __name__ == "__main__":
    function()