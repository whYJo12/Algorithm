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

    bojList.sort() # 사전 순 정렬
    bojList.sort(key=lambda x: len(x)) # 길이 순 정렬

    etcList.sort() # 사전 순 정렬
    etcList.sort(key=lambda x: len(x)) # 길이 순 정렬

    studyList = etcList + bojList

    for i in studyList:
        print(i)

if __name__ == "__main__":
    function()
