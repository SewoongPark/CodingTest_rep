#### n = 바구니의 개수
# m = m번의 횟수 내에서 바구니의 순서를 역순으로 변경


n, m = map(int, input().split())
baskets = []

for basket in range(1, n + 1):
        baskets.append(basket)
        
for changes in range(1, m + 1):
    i, j = map(int, input().split())
    i, j = i - 1, j
    
#i번째부터 j번째까지의 바구니의 순서를 역순으로 변경    
    baskets[i:j] = reversed(baskets[i:j])
print(*baskets)