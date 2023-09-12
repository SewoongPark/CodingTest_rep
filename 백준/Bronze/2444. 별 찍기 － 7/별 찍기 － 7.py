n = int(input())

# 윗 부분 출력
for i in range(n):
    print(" " * (n - i - 1) + "*" * ((i * 2) + 1))

# 아래 부분 출력
for i in range(n - 2, -1, -1): 
    print(" " * (n - i - 1) + "*" * ((i * 2) + 1))
