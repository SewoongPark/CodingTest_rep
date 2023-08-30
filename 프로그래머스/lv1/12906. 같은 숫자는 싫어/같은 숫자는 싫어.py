def solution(arr):
    answer = []
    que = []
    stack = []
    for num in range(0, len(arr)-1): #list범위를 벗어나기 때문에 1을 빼줌
      if arr[num] != arr[num + 1]: 
        #현재 인덱스와 다음 순서의 인덱스 요소 비교
        #한 개씩만 담아야 하니까 서로 같지 않은 요소들만 담는다
        answer.append(arr[num])
    answer.append(arr.pop()) 
    return answer