def solution(arr1, arr2):
    answer = []
    cnt = 0 #행의 길이(한 개의 리스트에 담긴 원소의 수)와 같을 때 리스트로 한번 더 감싸기
    changer = 0
    row = len(arr1)
    for a1, a2 in zip(arr1, arr2):
        totalList = []
        for idx, (num1, num2) in enumerate(zip(a1, a2)):
            totalList.append(num1 + num2)
        answer.append(totalList)
    return answer