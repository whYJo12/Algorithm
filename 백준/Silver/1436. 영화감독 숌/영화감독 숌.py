import sys

input = sys.stdin.readline
output = sys.stdout.write

def function():
    order = int(input())
    six = 666
    count = 0

    while True:
        if '666' in str(six):
            count += 1 #cnt번째 영화
        if count == order:
            return six
            break
        six += 1

if __name__ == "__main__":
    print(function())