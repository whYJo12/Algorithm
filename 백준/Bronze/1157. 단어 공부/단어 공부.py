def function():
    word = input().lower()
    wordList = list(set(word))
    cnt = []

    for i in wordList:
        count = word.count(i)
        cnt.append(count)

    if cnt.count(max(cnt)) >= 2:
        print("?")
    else:
        print(wordList[(cnt.index(max(cnt)))].upper())

if __name__ == "__main__":
    function()