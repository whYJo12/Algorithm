import sys

def function():
    N, M = map(int, sys.stdin.readline().split())
    passwordDictionary = {}

    for i in range(1, N+1):
        site, password = map(str, sys.stdin.readline().split())
        passwordDictionary[site] = password

    for i in range(M):
        question = sys.stdin.readline().strip()
        print(passwordDictionary[question])

if __name__ == "__main__":
    function()