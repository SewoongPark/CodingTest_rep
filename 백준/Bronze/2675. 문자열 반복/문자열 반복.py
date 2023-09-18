n = int(input())

for i in range(n):
    num, string = input().split()
    num = int(num)
    answer = ""

    for j in range(len(string)):
        answer += string[j] * num
    print(answer)