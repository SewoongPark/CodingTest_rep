n = int(input())
cnt =1
house = 1
while n > house:
  house += 6 * cnt
  cnt += 1
  
print(cnt)