import math
def solution(progresses, speeds):
  n = len(progresses)
  date_left = []
  answer = []
  
  
  for i in range(n):
    progresses_left = 100 - progresses[i]
    cuts = math.ceil(progresses_left / speeds[i])
    date_left.append(cuts)  


  while date_left:
    remain = date_left.pop(0)
    result = 1
    while len(date_left) != 0 and remain >= date_left[0]:
      result += 1
      date_left.pop(0)
    answer.append(result)
  return answer   
