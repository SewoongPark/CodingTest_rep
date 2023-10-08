n = int(input())

if n == 1:
    pass
else:
    div = 2 

    while n > 1:
        if n % div == 0:
            print(div)
            n //= div
        else:
            div += 1