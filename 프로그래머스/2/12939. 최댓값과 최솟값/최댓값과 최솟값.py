def solution(s):
    answer = []
    ns = s.split(" ")
    conv = ""
    for i in ns:
        i = int(i)
        answer.append(i)
    conv = str(min(answer)) +" "+ str(max(answer))
    return conv