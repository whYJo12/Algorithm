def function():
        T = int(input())

        for _ in range(T):
            R, S = input().split()

            for i in S:
                print(str(i)*int(R), end="")
            print()

if __name__ == "__main__":
    function()