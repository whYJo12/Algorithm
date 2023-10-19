import sys

input = sys.stdin.readline
output = sys.stdout.write

def function():
    a, b = input().split()
    setA = set(map(int, sys.stdin.readline().split()))
    setB = set(map(int, sys.stdin.readline().split()))

    diffAB = list(setA.difference(setB))
    diffBA = list(setB.difference(setA))

    symmetricDifference = len(diffAB)+len(diffBA)
    return symmetricDifference


if __name__ == "__main__":
    print(function())