def solution(s):
    answer = ''      
    for alp in s:
        lowers = sorted(s, reverse = True)
    answer = "".join(lowers)
    return answer
  
