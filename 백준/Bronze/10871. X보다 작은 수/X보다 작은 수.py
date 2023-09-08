#N의 제곱까지 가능
n, x = map(int, input().split())
a = list(input().split())

#for문으로 풀기
for i in a:
    i = int(i)
    if i < x:
        print(i, end = " ")