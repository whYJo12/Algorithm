import sys

def function():
    N = int(input())
    word = [input() for i in range(N)]
    word.sort(key=len)
    result = 0

    for i in range(N):
        flag = False
        # 현재 단어보다 길이가 긴 단어인지 확인
        for j in range(i+1, N):
            # 현재 단어가 접두사인지 확인
            if word[i] == word[j][0:len(word[i])]:
                flag = True
                break
        #현재 단어가 접두사가 아니라면 카운트 추가
        if not flag:
            result += 1

    print(result)

if __name__ == "__main__":
    function()