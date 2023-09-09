def main():
    n, m = map(int, input().split())
    baskets = list(range(1, n + 1))  # 초기 바구니 상태 (1부터 N까지의 공이 들어있음)

    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1  # 바구니 번호를 0부터 시작하는 인덱스로 변환
        j -= 1

        # 바구니 i와 바구니 j의 공을 교환
        baskets[i], baskets[j] = baskets[j], baskets[i]

    # 각 바구니에 들어있는 공의 번호 출력
    print(" ".join(map(str, baskets)))

if __name__ == "__main__":
    main()
