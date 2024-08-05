def solution(s):
    answer = ''  
    lowers, uppers = '', ''
    
    for alp in s:
        if alp == alp.lower():
            lowers = sorted(s, reverse = True)
    answer = "".join(lowers)
    return answer
  
