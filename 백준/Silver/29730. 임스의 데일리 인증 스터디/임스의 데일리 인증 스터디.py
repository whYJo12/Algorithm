def function():
    n = int(input())
    bojList = []
    etcList = []

    for _ in range(n):
        study = input()

        if 'boj.kr/' in study:
            bojList.append(study)
        else:
            etcList.append(study)

    bojList.sort()
    bojList.sort(key=lambda x: len(x))

    etcList.sort()
    etcList.sort(key=lambda x: len(x))

    studyList = etcList + bojList

    for i in studyList:
        print(i)

if __name__ == "__main__":
    function()