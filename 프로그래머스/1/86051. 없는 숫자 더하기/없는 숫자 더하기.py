def solution(numbers):
    nums = list(range(0, 10))
    answer = [n for n in nums if n not in numbers]
    return sum(answer)
    # for n in nums:
    #     if n not in numbers:   
    #        answer += n
    # return answer