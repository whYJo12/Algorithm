def function():
    N = int(input())
    dasom = int(input())
    votesList = []
    for _ in range(N - 1):
        votesList.append(int(input()))
    buy = 0

    votesList.sort(reverse=True)

    if N == 1:
        print(0)
    else:
        while votesList[0] >= dasom:
            dasom += 1
            buy += 1
            votesList[0] -= 1
            votesList.sort(reverse=True)
        print(buy)

if __name__ == "__main__":
    function()
