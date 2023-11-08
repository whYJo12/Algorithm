def function():
    T = int(input())  # 테스트 케이스 수

    for _ in range(T):  # 테스트 케이스 수 만큼 반복        
        J, N = map(int, input().split())
        boxSize = []
        for i in range(N):
            R,C = map(int, input().split()) # 상자 가로세로 길이를 입력받아 저장
            boxSize.append(R * C) # 상자크기 (가로*세로)

        boxSize.sort(reverse=True) # 상자크기를 내림차순으로 정렬

        count = 0
        while J > 0:
            J -= boxSize[count]  # 사탕을 박스에 넣었으니 사탕갯수를 박스사이즈만큼 빼기
            count += 1  # 상자가 1개 쓰였으니 카운트세기

        print(count)

if __name__ == "__main__":
    function()