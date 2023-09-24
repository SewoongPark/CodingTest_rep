n, m = map(int, input().split())

alpha_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''

if n == 0:
    result = '0'

while n > 0:
    remainder = n % m  
    result = alpha_list[remainder] + result  
    n //= m  


print(result)