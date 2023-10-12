list = [input() for _ in range(2)]
a = int(list[0])
b = int(list[1])

if a > 0 and b > 0:
    print(1)
elif a < 0 and b > 0:
    print(2)
elif a < 0 and b < 0:
    print(3)
else:
    print(4)

