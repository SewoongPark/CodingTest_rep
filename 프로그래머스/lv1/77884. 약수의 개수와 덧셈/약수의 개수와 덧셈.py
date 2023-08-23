def solution(left, right):
# 1. left, right의 약수의 개수를 각각 구한다
# 2. 약수의 개수가 짝수면 수를 더하고 홀수면 총합에서 뺀다
  arr = []
  arr2 = []
  cnt = 0
  for numbers in range(left, right+1): # numbers: left부터 right까지의 수
    arr = [] #한 수의 약수 배열이 끝났을때, 다른 수로 넘어가기 위해 초기화
    for number in range(1, numbers+1): 
      if numbers % number == 0: # numbers의 약수를 구한다
        arr.append(number)
        arr2=[numbers]
    for cnt_num in arr2: 
      if len(arr) % 2==0: 
        cnt+=cnt_num
      else:
        cnt -= cnt_num
  return cnt
solution(24, 27)