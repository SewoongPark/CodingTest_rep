#O(N ^ 2)
n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums), end = " ")
