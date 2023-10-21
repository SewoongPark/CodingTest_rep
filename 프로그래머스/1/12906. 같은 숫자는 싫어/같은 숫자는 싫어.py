import itertools

def solution(arr):
    stack = []
    cnt = 0
    for i in arr:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
    return stack