def function():
    S = list(map(str, input()))
    count = 0

    for i in range(len(S)-1):
        if S[i] != S[i+1]:  #0>1, 1>0 일때만 카운트
            count += 1
    print((count + 1) // 2) 
    
    # 입력받은 string -> 변화횟수 -> 뒤집어야할 횟수
    # 0 -> 0 -> 0
    # 01 -> 1 -> 1
    # 010 -> 2 -> 1
    # 0101 -> 3 -> 2
    # 01010 -> 4 -> 2
    # 010101 -> 5 -> 3
    # -> 횟수에 +1을 하고 몫을 가져오면 뒤집어야할 횟수가 나옴
    
if __name__ == "__main__":
    function()