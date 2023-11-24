def solution(array, commands):
    answer = []
    for com in commands:
        # com의 1, 2번째 원소 값만큼 슬라이싱한다
        arr = sorted(array[com[0]-1:com[1]])
        answer.append(arr[com[2]-1])
        # array에서 슬라이싱 한 값을 정렬한다
        # com의 3번째 원소에 해당하는 array의 값을 반환한다
    return answer