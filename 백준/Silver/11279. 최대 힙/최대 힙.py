import sys
import heapq

def function():
    N = int(sys.stdin.readline())
    heap = []

    for _ in range(N):
        oper = int(sys.stdin.readline())
        
        if oper != 0:
            heapq.heappush(heap, (-oper, oper))
        elif oper == 0 and len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

if __name__ == "__main__":
    function()