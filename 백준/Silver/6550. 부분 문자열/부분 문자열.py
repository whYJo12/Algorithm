def function():

    while True:
        try:
            s, t = map(str, input().split())
            sList = list(s)
            for i in t: #문자열 t안의 알파벳이
                if sList and i == sList[0]: #리스트가 비어있지않고 & sList의 첫번째 알파벳과 같다면
                    sList.pop(0)    #리스트에서 해당 알파벳 제거

            if not sList:   #리스트가 비어있다면 = 부분문자열
                print('Yes')
            else:
                print('No')

        except:
            break

if __name__ == "__main__":
    function()