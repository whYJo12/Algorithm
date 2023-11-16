import sys
import heapq

def function():
    N = int(sys.stdin.readline())
    heap = []
    for _ in range(N):
        oper = int(sys.stdin.readline())

        if oper != 0:
            heapq.heappush(heap, oper)
        elif oper == 0 and len(heap) != 0:
            print(heap[0])
            heapq.heappop(heap)
        else:
            print(0)

if __name__ == "__main__":
    function()