string = input().lower()  # 입력 문자열을 소문자로 변환하여 처리

alphabets = {}  # 알파벳 빈도를 저장할 딕셔너리

for alpha in string:
    if alpha.isalpha():  # 알파벳인 경우에만 처리
        if alpha in alphabets:
            alphabets[alpha] += 1
        else:
            alphabets[alpha] = 1

max_count = max(alphabets.values())  # 가장 많이 사용된 알파벳의 빈도

most_common = [alpha for alpha, count in alphabets.items() if count == max_count]

if len(most_common) == 1:
    print(most_common[0].upper())
else:
    print("?")