N = int(input())
chicken = list(map(int, input().split()))
k = int(input())

index = N // k
sortChicken = []

for i in range(0, N, index):
    sortChicken = chicken[i:i+index]
    sortChicken.sort()
    for j in sortChicken:
        print(j, end=' ')
