def solution(s):
    answer = []
    stack = []
    cnt = 0    
    
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
        
