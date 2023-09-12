n = int(input())
total_len = 2 * (int(n) - 1)

for i in range(n):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))
#     if i > 8:
        
for i in range(n-1):
    print(" "*(i + 1) + "*" * (-2 * i + (2*n -3)))