num1, num2 = map(str, input().split())
num1,num2 = int(num1[::-1]), int(num2[::-1])
if num1 - num2 < 0:
    print(num2)
else:
    print(num1)