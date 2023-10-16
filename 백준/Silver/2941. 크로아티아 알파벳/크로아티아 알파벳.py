word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in croatia:
    if i in word:
        word = word.replace(i, "a")
count += len(word)

print(count)

