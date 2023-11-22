import sys
def my_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

def function():
    N = int(input())
    if N != 0:
        level = list(int(sys.stdin.readline()) for _ in range(N))
        level.sort(reverse=True)

        trimmedMean = my_round(N * 0.15)

        apply_truc = sorted(level)[trimmedMean: N - trimmedMean]
        mean = my_round(sum(apply_truc) / len(apply_truc))

        print(mean)
    else:
        print(0)

if __name__ == "__main__":
    function()