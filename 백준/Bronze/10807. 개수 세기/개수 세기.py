#N의 세제곱까지 가능
n = int(input())
nums = list(input().split())
target = input()
cnt = 0
# for문으로 풀기
for i in nums:
    if  i == target:
        cnt += 1
print(cnt)