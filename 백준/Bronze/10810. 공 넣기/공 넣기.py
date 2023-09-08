m, n = map(int, input().split())
basket_dict = {}

for num in range(n):
    i, j, ball = map(int, input().split())
    ball = str(ball)
    for idx, basket in enumerate(range(i, j + 1)):
        # 바구니를 정의한다
        if f'{basket}' not in basket_dict or basket_dict[f'{basket}'] != ball:
            basket_dict[f'{basket}'] = ball

# 모든 바구니가 채워지지 않았다면 0으로 채워준다
for basket in range(1, m + 1):
    if f'{basket}' not in basket_dict:
        basket_dict[f'{basket}'] = '0'

# 바구니에 들어있는 공의 번호를 출력
result = " ".join([basket_dict[f'{basket}'] for basket in range(1, m + 1)])
print(result)
