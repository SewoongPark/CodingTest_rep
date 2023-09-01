def solution(n):
  answer = ''
  while n > 0:
    n, remain = divmod(n, 3)
    answer += str(remain)
    n_answer = int(answer, 3)
  return n_answer