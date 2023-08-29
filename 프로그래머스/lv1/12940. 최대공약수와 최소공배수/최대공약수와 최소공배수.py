def solution(n, m):
    answer = []
    arr = []
    arr2 = []
    for num in range(1, m+1):
    # 최대공약수 구하기
      if n % num == 0 and m % num == 0:
        arr.append(num)
        max_num = arr[-1]
    # 최소공배수 구하기
    for min in range(1,(n * m)+1):
      if min % n == 0 and min % m == 0:
        arr2.append(min)
        min_num = arr2[0]
    answer = [max_num, min_num]
    return answer        
  