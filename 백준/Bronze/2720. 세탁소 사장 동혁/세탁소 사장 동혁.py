total = int(input())

coins = [25, 10, 5, 1]

for i in range(total):
    m = int(input())
    remaining = m  
    
    for coin in coins:
        num_coins = remaining // coin
        remaining %= coin
        print(num_coins, end=" ") 
    print()
    