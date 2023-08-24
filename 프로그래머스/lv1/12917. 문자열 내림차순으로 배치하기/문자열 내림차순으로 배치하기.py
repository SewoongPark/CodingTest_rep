def solution(s):
  answer = ''
  uppercase = ""
  upper_char = ""
  arr = []
  upper_arr = []
  length = len(s)
  for alpha in range(length):
    arr.append(s[alpha]) # 전체 알파벳 담기
    if s[alpha].isupper()==True:
      uppercase = arr.pop() #대문자만 빼내기
      upper_arr.append(uppercase) #대문자 따로 담기
      upper_arr = sorted(upper_arr, reverse = True) #대문자 리스트 정렬
  
  for upper_alpha in upper_arr:
      upper_char += upper_alpha #대문자만 문자열로 변환
      print(upper_char)
  arr = sorted(arr, reverse = True) #대문자 빼낸 알파벳 리스트 정렬
  for n_alpha in arr:
    answer += n_alpha 

  answer = answer+upper_char
  return answer 
solution("adFaQZs")