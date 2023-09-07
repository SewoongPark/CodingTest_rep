def solution(d, budget):
    answer = 0
    cnt = 0
    d = sorted(d)
    
    for i in range(len(d)):
        answer += d[i]
        cnt += 1
        if sum(d) == budget:
            return len(d)
        elif answer > budget:
            break
        elif sum(d) < budget:
            if cnt == len(d):
                return cnt
        elif answer == budget:
            return cnt
    return i
        