def solution(s):
  # 모든 단어의 첫 문자는 대문자로 바꾸기
  # 첫 문자가 숫자일때는 이어지는 알파벳을 소문자로
  spaces = s.split(" ")
  arr = []
  conv = ""
  for idx, alpha in enumerate(spaces):
    if alpha != "":
      arr.append((alpha[0].replace(alpha[0], alpha[0].upper())+ alpha[1:].lower()))
    else:
      # 공백 문자가 여러번 나올 경우
      arr.append("")
    conv = " ".join(arr)  
  return conv   