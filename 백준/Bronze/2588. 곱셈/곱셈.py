# 두 개의 세 자리 수를 입력으로 받습니다.
n = input()
m = input()

# 입력된 문자열이 세 자리가 맞는지 확인합니다.
if len(n) != 3 or len(m) != 3:
    print("세 자리 수를 입력해주세요.")
else:
    # (3), (4), (5)를 계산합니다.
    mul3 = int(n) * int(m[2])
    mul4 = int(n) * int(m[1])
    mul5 = int(n) * int(m[0])

    # (6)를 계산합니다.
    mul6 = int(n) * int(m)

    # 결과를 출력합니다.
    print(mul3)
    print(mul4)
    print(mul5)
    print(mul6)