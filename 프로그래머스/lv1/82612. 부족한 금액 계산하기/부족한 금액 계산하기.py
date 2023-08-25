def solution(price, money, count):
    answer = 0
    for cnt in range(1, count+1):
      total_price = price * cnt
      answer += total_price
    if answer > money:
      answer = answer - money
    else:
      answer = 0
    return answer