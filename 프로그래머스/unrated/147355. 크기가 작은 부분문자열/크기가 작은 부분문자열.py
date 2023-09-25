def solution(t, p):
  answer = 0
  
  for i in range(len(t)):
    string = t[i : len(p) + i]
      
    
    if len(string) == len(p):
      string = int(string)
      if string == int(p) or string < int(p):
        answer += 1
  return answer