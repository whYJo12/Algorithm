import sys

input = sys.stdin.readline
output = sys.stdout.write
import re

def function():
    size = int(input())
    queue = []
    count = 0

    while True:
        order = input()
        count += 1
        if 'push' in order:
            queue.append(re.sub(r'[^0-9]', '', order))
        if 'pop' in order:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
                queue.pop(0)
        if 'front' in order:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        if 'back' in order:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[len(queue)-1])
        if 'size' in order:
            print(len(queue))
        if 'empty' in order:
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        if count == size:
            break



if __name__ == "__main__":
    function()