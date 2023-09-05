def solution(s):
    answer = ''
    # 짝수번째 알파벳은 대문자로
    # 홀수번째 알파벳은 소문자로
    
    # 공백을 구분해서 나눈 단어들의 인덱스를 조회
    s = s.split(" ")
    zzac = []
    hol = []
    
    for alpha in s:
        for i, alp in enumerate(alpha):
            if i % 2 == 0:
                answer += alp.upper()
            else:
                answer += alp.lower()
        answer += " "
    return answer[:-1]
