def function():
    N = int(input())
    M = int(input())
    S = input()
    P = ""
    count = 0

    for i in range(0, N):
        if N != i:
            P += "IO"
    P += "I"

    

    for i in range(len(S) - len(P)+1):
        if S[i:i+len(P)] == P:
            count += 1

    print(count)

if __name__ == "__main__":
    function()