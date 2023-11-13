import sys

def function():
    N, M = map(int, sys.stdin.readline().split())
    by_id = {}
    by_name = {}

    for i in range(1, N+1):
        poketmon = sys.stdin.readline().strip()
        by_id[i] = poketmon
        by_name[poketmon] = i

    for i in range(M):
        question = sys.stdin.readline().strip()
        if question.isdigit() == True:   #질문이 숫자로 들어온다면
            print(by_id[int(question)])
        else:
            print(by_name[question])

if __name__ == "__main__":
    function()