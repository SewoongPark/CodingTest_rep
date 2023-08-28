a, b = map(int, input().strip().split(' '))
for row in range(1, b+1):
    for col in range(1, a+1):
        # print(row, col, row * "*", col*"*")
        if col == a:
            print(col*"*")