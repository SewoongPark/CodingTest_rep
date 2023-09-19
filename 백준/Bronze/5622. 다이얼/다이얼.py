alpha = input()
alp_dict = { 'ABC': 3, 'DEF':4, 'GHI': 5, 'JKL':6, 
            'MNO':7, 'PQRS':8,'TUV':9,'WXYZ':10}
answer = 0
for alp in alpha:
    for k, v in alp_dict.items():
        if alp in k:
            answer += v
print(answer)