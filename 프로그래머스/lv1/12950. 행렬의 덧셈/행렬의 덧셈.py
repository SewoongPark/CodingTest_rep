def solution(arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        totalList = []
        for num1, num2 in zip(a1, a2):
            totalList.append(num1 + num2)
        answer.append(totalList)
    return answer
