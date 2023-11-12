def solve(n):
   if n == 1:   #분할정복이 계속되어 n이 1이되었을때
       return "-"
   else:
       left = solve(n // 3)
       center = " " * (n // 3)
       return left + center + left  #좌우가 같기때문에 left를 두번더함

if __name__ == "__main__":
    while True:
        try:
            N = int(input())
            rst = solve(3 ** N)
            print(rst)
        except:
            break
