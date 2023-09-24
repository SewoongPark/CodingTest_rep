n, m = input().split()
m = int(m)
# 입력 받은 n의 10진수 값을 저장
  # n이 'A'일 경우 10 반환
alpha_list = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

num_list = list(range(36))
answer = 0

for i, char in enumerate(n):
  num_idx = alpha_list.index(char)
  # M진법의 거듭제곱을 구하고 지수를 곱해서 다 더해줌
  answer += (num_list[num_idx] * (m**(len(n)-1-i)))
print(answer)