def function():
    N = int(input())

    for i in range(1, 10):
        print(str(N) + " * " + str(i) + " = " + str(N*i))

if __name__ == "__main__":
    function()