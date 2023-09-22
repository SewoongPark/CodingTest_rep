# 다섯 줄의 입력을 받아서 각 줄을 리스트에 저장
words = [input() for _ in range(5)]

# 가장 긴 단어의 길이 구함, 가장 긴 행을 기준으로 순회해야 인덱스 에러가 발생하지 않기 때문
max_length = max(len(word) for word in words)

result = ""

# 열 단위로 순회하면서 세로로 읽어서 결과에 추가
for i in range(max_length):
    for word in words:
        if i < len(word):  # 현재 단어에 글자가 존재하면 추가
            result += word[i]

print(result)
