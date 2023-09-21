# 9x9 격자판 입력 받기
grid = []
for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

# 최댓값과 그 위치 초기화
max_value = -1
max_row, max_col = -1, -1

# 격자판 순회하며 최댓값 찾기
for row in range(9):
    for col in range(9):
        if grid[row][col] > max_value:
            max_value = grid[row][col]
            max_row, max_col = row, col

# 결과 출력
print(max_value)
print(max_row + 1, max_col + 1)  
